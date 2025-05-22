<template>
  <div class="card h-100">
    <img
      v-if="content.image_url"
      :src="content.image_url"
      class="card-img-top"
      :alt="`Bild zu ${content.title}`"
      loading="lazy"
    />

    <div :class="['card-body', { expanded }]" ref="textBlock">
      <h5 class="card-title">{{ content.title }}</h5>
      <p class="card-text">{{ content.description }}</p>

      <div v-if="!expanded && isOverflowing" class="fade-out" />

      <small
        v-if="isOverflowing || expanded"
        class="toggle-text text-info"
        @click="expanded = !expanded"
      >
        {{ expanded ? "Weniger ▲" : "Mehr ▼" }}
      </small>
    </div>

    <div class="card-footer">
      <NuxtLink
        v-if="content.has_view"
        :to="`/content/${content.id}`"
        class="btn btn-info btn-sm"
      >
        View Details
      </NuxtLink>
      <a
        v-else
        :href="content.links?.github"
        class="btn btn-info btn-sm"
        target="_blank"
        rel="noopener noreferrer"
      >
        View on GitHub
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch, nextTick, onBeforeUnmount } from "vue";
import type { Content } from "@/types/content";

defineProps<{ content: Content }>();

const expanded = ref(false);
const isOverflowing = ref(false);
const textBlock = ref<HTMLElement | null>(null);

let observer: ResizeObserver | null = null;

const checkOverflow = () => {
  if (textBlock.value) {
    const el = textBlock.value;
    isOverflowing.value = el.scrollHeight > el.clientHeight;
  }
};

onMounted(() => {
  nextTick(() => {
    if (textBlock.value) {
      observer = new ResizeObserver(() => checkOverflow());
      observer.observe(textBlock.value);
    }
    checkOverflow();
  });
});

onBeforeUnmount(() => {
  if (observer && textBlock.value) {
    observer.unobserve(textBlock.value);
  }
});
</script>

<style scoped>
.card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}

.card:hover {
  transform: translateY(-5px) scale(1.02);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

.card-img-top {
  height: 350px;
  width: 100%;
  object-fit: cover;
  object-position: center;
}

.card-body {
  position: relative;
  max-height: 140px; /* oder dein Zielwert */
  overflow: hidden;
  transition: max-height 0.3s ease;
  padding-bottom: 2rem;
}

/* nur bei erweitertem Text */
.card-body.expanded {
  max-height: 1000px;
  padding-bottom: 0;
}

.fade-out {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 2.5rem;
  width: 100%;
  background: linear-gradient(to top, white, transparent);
  pointer-events: none;
  z-index: 1;
}

.card-title {
  margin-bottom: 0.5rem;
  transition: color 0.2s ease;
}

.card:hover .card-title {
  color: #38b4a8;
}

.toggle-text {
  position: absolute;
  bottom: 0.3rem;
  right: 0.7rem;
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
  z-index: 2;
  background-color: white;
  padding: 0 0.3rem;
  transition: color 0.2s ease;
  color: #38b4a8;
}

.toggle-text:hover {
  text-decoration: underline;
}
</style>
