<script setup lang="ts">
import { computed, watchEffect } from 'vue';
import { useRoute } from 'vue-router';
import { projects } from '../data/projects';
import ProjectCard from '../components/ProjectCard.vue';
import SiteNav from '../components/SiteNav.vue';
import SiteFooter from '../components/SiteFooter.vue';

const route = useRoute();
const project = computed(() => projects.find((p) => p.slug === route.params.slug));

watchEffect(() => {
  document.title = project.value
    ? `${project.value.nombre} | Cordova Solutions`
    : 'Proyecto no encontrado | Cordova Solutions';
});
</script>

<template>
  <SiteNav />

  <main class="py-16 bg-paper min-h-[60vh]">
    <div class="max-w-4xl mx-auto px-6">
      <RouterLink to="/#proyectos"
                  class="inline-flex items-center gap-2 text-sm font-bold text-ink/60 hover:text-accent-600 transition-colors mb-8">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
        Volver a Casos de Éxito
      </RouterLink>

      <ProjectCard v-if="project" :project="project" />

      <div v-else class="text-center py-20 bg-ink/[0.03] rounded-2xl border border-dashed border-ink/15">
        <p class="text-ink/60 mb-4">No encontramos ese proyecto.</p>
        <RouterLink to="/#proyectos" class="font-bold text-accent-600 hover:text-accent-700 transition-colors">
          Ver todos los Casos de Éxito →
        </RouterLink>
      </div>
    </div>
  </main>

  <SiteFooter />
</template>
