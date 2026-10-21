<script setup lang="ts">
import type { Project } from '../data/projects';

defineProps<{
  project: Project;
}>();
</script>

<template>
  <div class="group bg-white border border-slate-200 rounded-xl overflow-hidden hover:shadow-xl transition-all duration-300">
    <div class="flex flex-col lg:flex-row">
      <!-- Referential Illustration -->
      <img :src="project.ilustracion"
           :alt="`Ilustración referencial: ${project.nombre}`"
           class="w-full lg:w-56 h-40 lg:h-auto object-cover flex-shrink-0 bg-slate-50" />

      <div class="p-8 flex-1">
        <div class="flex flex-wrap justify-between items-start mb-4 gap-4">
          <div>
            <span class="text-xs font-bold tracking-widest text-slate-400 uppercase">{{ project.categoria }}</span>
            <h3 class="text-2xl font-bold text-slate-900 mt-1">{{ project.nombre }}</h3>
            <p v-if="project.cliente" class="text-slate-500 font-medium">Cliente: {{ project.cliente }}</p>
          </div>
          <span v-if="project.status"
                class="px-3 py-1 rounded-full text-xs font-semibold"
                :class="project.status === 'Completado' ? 'bg-green-50 text-green-700 border border-green-200' : 'bg-amber-50 text-amber-700 border border-amber-200'">
            {{ project.status }}
          </span>
        </div>

        <div class="mb-6">
          <h4 class="text-sm font-bold text-slate-900 uppercase tracking-wider mb-2">Problema Resuelto</h4>
          <p class="text-slate-600 leading-relaxed">{{ project.problemaResuelto }}</p>
        </div>

        <div class="mb-6">
          <h4 class="text-sm font-bold text-slate-900 uppercase tracking-wider mb-3">Proceso</h4>
          <ol class="space-y-2">
            <li v-for="(paso, i) in project.proceso" :key="i" class="flex gap-3 text-slate-600 text-sm leading-relaxed">
              <span class="flex-shrink-0 w-5 h-5 rounded-full bg-slate-900 text-white text-[11px] font-bold flex items-center justify-center mt-0.5">{{ i + 1 }}</span>
              <span>{{ paso }}</span>
            </li>
          </ol>
        </div>

        <div class="flex flex-wrap gap-2">
          <span v-for="tech in project.tecnologias" :key="tech"
                class="px-2.5 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded border border-slate-200">
            {{ tech }}
          </span>
        </div>
      </div>
    </div>

    <!-- Maqueta referencial (HTML/CSS/Bootstrap, sin datos ni accesos reales) -->
    <div class="border-t border-slate-100 bg-slate-50 p-6">
      <div class="flex items-center justify-between mb-3">
        <h4 class="text-sm font-bold text-slate-900 uppercase tracking-wider">Vista de la Solución</h4>
        <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wide">Maqueta referencial</span>
      </div>
      <div class="rounded-lg border border-slate-200 bg-white overflow-hidden shadow-sm">
        <div class="flex items-center gap-1.5 px-3 py-2 bg-slate-100 border-b border-slate-200">
          <span class="w-2.5 h-2.5 rounded-full bg-red-300"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-amber-300"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-green-300"></span>
          <span class="ml-3 text-[11px] text-slate-400 font-mono">maqueta — datos de ejemplo</span>
        </div>
        <iframe :src="project.mockup"
                title="Maqueta referencial de la solución"
                loading="lazy"
                class="w-full"
                :class="project.mockupAlto ?? 'h-80'"
                sandbox="allow-same-origin allow-scripts"></iframe>
      </div>
    </div>
  </div>
</template>
