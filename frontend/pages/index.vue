<template>
  <section>
    <h1>Projekte</h1>

    <div v-if="pending" class="alert alert-info">Loading…</div>
    <div v-else-if="error" class="alert alert-danger">
      Error: {{ error.message }}
    </div>

    <div class="px-5">
      <div class="row">
        <div class="col-md-4 mb-4" v-for="item in entries" :key="item.id">
          <CardContent :content="item" />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import CardContent from "~/components/CardContent.vue";
import { useContent } from "~/composables/useContent";

const { fetchContent } = useContent();

const {
  data: entries,
  pending,
  error,
} = await useLazyAsyncData("content", fetchContent);
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
