<template>
  <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" class="form-control" />
    </div>

    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea name="description" class="form-control"></textarea>
    </div>

    <div class="form-group mb-3">
      <label for="poster" class="form-label">Poster</label>
      <input type="file" name="poster" class="form-control" />
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>

<script setup>
import { ref, onMounted } from "vue";

// Reactive variable to store CSRF token
let csrf_token = ref("");

// Function to fetch CSRF token from Flask
function getCsrfToken() {
  fetch("/api/v1/csrf-token")
    .then(response => response.json())
    .then(data => {
      csrf_token.value = data.csrf_token;
      console.log("CSRF token fetched:", csrf_token.value);
    })
    .catch(error => console.log("Error fetching CSRF token:", error));
}

// Call getCsrfToken when the component mounts
onMounted(() => {
  getCsrfToken();
});

// Function to submit the form using Fetch API
function saveMovie() {
  let movieForm = document.getElementById("movieForm");
  let form_data = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      "X-CSRFToken": csrf_token.value
    }
  })
    .then(response => response.json())
    .then(data => {
      console.log("Server response:", data);
      // TODO: Add success/error message display here
    })
    .catch(error => console.log("Error submitting form:", error));
}
</script>

<style scoped>
.form-group {
  margin-bottom: 1rem;
}
</style>