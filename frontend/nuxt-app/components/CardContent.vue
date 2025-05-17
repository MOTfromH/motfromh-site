<template>
  <div class="card h-100">
    <img
      v-if="content.image_url"
      :src="content.image_url"
      class="card-img-top"
      alt="Bild zu {{ content.title }}"
    />
    <div class="card-body">
      <h5 class="card-title">{{ content.title }}</h5>
      <p class="card-text">{{ content.description }}</p>
    </div>
    <div class="card-footer">
      <NuxtLink
        v-if="content.has_view"
        :to="`/content/${content.id}`"
        class="btn btn-info"
      >
        View Details
      </NuxtLink>
      <a
        v-else
        :href="content.links?.github"
        class="btn btn-info"
        target="_blank"
        rel="noopener noreferrer"
      >
        View on GitHub
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Content } from "@/types/content";
defineProps<{ content: Content }>();
</script>
