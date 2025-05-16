<template>
  <section>
    <h1>Content Dashboard</h1>

    <div v-if="pending" class="alert alert-info">Loading…</div>
    <div v-else-if="error" class="alert alert-danger">
      Error: {{ error.message }}
    </div>

    <div v-else class="row">
      <div class="col-md-4 mb-4" v-for="item in entries" :key="item.id">
        <!-- Hier wird die Card-Komponente gerendert -->
        <CardContent :content="item" />
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import CardContent from "~/components/CardContent.vue";
import type { Content } from "~/types/content";

// 1) fetch nur einmal pro Seite
const {
  data: entries,
  pending,
  error,
} = await useFetch<Content[]>("http://localhost:8001/api/v1/content/");
</script>

<style scoped>
.row {
  display: flex;
  flex-wrap: wrap;
}
.col-md-4 {
  flex: 0 0 33.333%;
  padding: 0 0.5rem;
}
.mb-4 {
  margin-bottom: 1.5rem;
}
</style>
