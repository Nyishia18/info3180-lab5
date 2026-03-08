<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <RouterLink class="navbar-brand" to="/">VueJS with Flask</RouterLink>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/about">About</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/movies">Movies</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/movies/create">Add Movie</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<style scoped>
/* Ensure navbar doesn't overlap content */
.navbar {
  margin-bottom: 2rem;
}
</style>