<template>
  <div class="container">
    <div v-if="message" class="alert alert-success">{{ message }}</div>
    <div v-if="errors.length > 0" class="alert alert-danger">
      <ul>
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
    </div>

    <form @submit.prevent="saveMovie" id="movieForm">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea name="description" class="form-control"></textarea>
      </div>
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Movie Poster</label>
        <input type="file" name="poster" class="form-control" />
      </div>
      <button type="submit" class="btn btn-primary" :disabled="loading">Save Movie</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let csrf_token = ref("");
let message = ref("");
let errors = ref([]);
let loading = ref(false);

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    });
}

onMounted(() => {
  getCsrfToken();
});

function saveMovie() {
  if (loading.value) return;
  loading.value = true;

  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
  .then(response => response.json())
  .then(data => {
    if (data.errors) {
      errors.value = data.errors;
      message.value = "";
    } else {
      message.value = data.message;
      errors.value = [];
      movieForm.reset();
    }

    loading.value = false;
  })
  .catch(error => {
    console.log(error);
    loading.value = false;
  });
}
</script>


