<template>
  <div class="container d-flex flex-wrap">
    <div v-for="movie in movies" :key="movie.id" class="card m-2" style="width: 18rem;">
      <img :src="movie.poster" class="card-img-top" :alt="movie.title">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text">{{ movie.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

const fetchMovies = () => {
  fetch('/api/v1/movies')
    .then(res => res.json())
    .then(data => movies.value = data.movies)
    .catch(err => console.log(err));
}

onMounted(() => {
  fetchMovies();
});
</script>