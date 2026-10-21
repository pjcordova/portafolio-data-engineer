<script setup lang="ts">
import type { Project } from '../data/projects';

defineProps<{
  project: Project;
}>();

const emit = defineEmits<{
  open: [];
}>();
</script>

<template>
  <button type="button"
          class="group w-full text-left bg-white border border-ink/10 rounded-xl overflow-hidden transition-shadow duration-300 hover:shadow-xl hover:shadow-ink/5 btn-press"
          @click="emit('open')">
    <div class="h-48 overflow-hidden bg-paper relative">
      <img :src="project.ilustracion"
           :alt="`Ilustración referencial: ${project.nombre}`"
           class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
      <span v-if="project.status"
            class="absolute top-3 right-3 px-2.5 py-0.5 rounded-full text-[11px] font-semibold"
            :class="project.status === 'Completado' ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' : 'bg-amber-50 text-amber-700 border border-amber-200'">
        {{ project.status }}
      </span>
    </div>
    <div class="p-6">
      <span class="text-xs font-bold tracking-widest text-ink/60 uppercase">{{ project.categoria }}</span>
      <h3 class="text-2xl font-serif italic font-normal text-ink mt-1 mb-2">{{ project.nombre }}</h3>
      <p class="text-ink/60 text-sm leading-relaxed line-clamp-2">{{ project.problemaResuelto }}</p>
      <span class="mt-4 inline-flex items-center gap-1.5 text-sm font-bold text-accent-600">
        Ver detalles
        <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
      </span>
    </div>
  </button>
</template>
