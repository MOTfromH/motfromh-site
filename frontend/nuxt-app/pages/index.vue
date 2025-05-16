<template>
  <h1>Raw API Output</h1>
  <pre>{{ entries }}</pre>
  <div v-if="error" class="error">Error: {{ error.message }}</div>
</template>

<script setup lang="ts">
// 1) first data fetch
const { data: entries, error } = await useFetch(
  "http://localhost:8001/api/v1/content/"
);
</script>

<style scoped>
.error {
  color: red;
}
</style>
