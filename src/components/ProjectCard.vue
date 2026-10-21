<script setup lang="ts">
import type { Project } from '../data/projects';

defineProps<{
  project: Project;
}>();
</script>

<template>
  <div class="group bg-white border border-ink/10 rounded-xl overflow-hidden transition-shadow duration-300 hover:shadow-xl hover:shadow-ink/5">
    <div class="flex flex-col lg:flex-row">
      <!-- Referential Illustration -->
      <div class="w-full lg:w-56 h-40 lg:h-auto flex-shrink-0 overflow-hidden bg-paper">
        <img :src="project.ilustracion"
             :alt="`Ilustración referencial: ${project.nombre}`"
             class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
      </div>

      <div class="p-8 flex-1">
        <div class="flex flex-wrap justify-between items-start mb-4 gap-4">
          <div>
            <span class="text-xs font-bold tracking-widest text-ink/60 uppercase">{{ project.categoria }}</span>
            <h3 class="text-2xl font-serif italic font-normal text-ink mt-1">{{ project.nombre }}</h3>
            <p v-if="project.cliente" class="text-ink/60 font-medium">Cliente: {{ project.cliente }}</p>
          </div>
          <span v-if="project.status"
                class="px-3 py-1 rounded-full text-xs font-semibold"
                :class="project.status === 'Completado' ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' : 'bg-amber-50 text-amber-700 border border-amber-200'">
            {{ project.status }}
          </span>
        </div>

        <div class="mb-6">
          <h4 class="text-sm font-bold text-ink uppercase tracking-wider mb-2">Problema Resuelto</h4>
          <p class="text-ink/60 leading-relaxed">{{ project.problemaResuelto }}</p>
        </div>

        <div class="mb-6">
          <h4 class="text-sm font-bold text-ink uppercase tracking-wider mb-3">Proceso</h4>
          <ol class="space-y-2">
            <li v-for="(paso, i) in project.proceso" :key="i" class="flex gap-3 text-ink/60 text-sm leading-relaxed">
              <span class="flex-shrink-0 w-5 h-5 rounded-full bg-ink text-paper text-[11px] font-bold flex items-center justify-center mt-0.5">{{ i + 1 }}</span>
              <span>{{ paso }}</span>
            </li>
          </ol>
        </div>

        <div v-if="project.resultados?.length" class="mb-6 bg-accent-50 border border-accent-100 rounded-lg p-4">
          <h4 class="text-sm font-bold text-ink uppercase tracking-wider mb-2">Resultados</h4>
          <ul class="space-y-1.5">
            <li v-for="(r, i) in project.resultados" :key="i" class="flex gap-2 text-sm text-ink/70 leading-relaxed">
              <span class="text-accent-600 font-bold">→</span>
              <span>{{ r }}</span>
            </li>
          </ul>
        </div>

        <div class="flex flex-wrap gap-2">
          <span v-for="tech in project.tecnologias" :key="tech"
                class="px-2.5 py-1 bg-ink/[0.04] text-ink/70 text-xs font-medium rounded border border-ink/10">
            {{ tech }}
          </span>
        </div>
      </div>
    </div>

    <!-- Maqueta referencial (HTML/CSS/Bootstrap, sin datos ni accesos reales) -->
    <div class="border-t border-ink/10 bg-ink/[0.02] p-6">
      <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-ink uppercase tracking-wider">Vista de la Solución</h4>
        <div class="flex items-center gap-3">
          <a v-if="project.linkSitio" :href="project.linkSitio" target="_blank" rel="noopener"
             class="inline-flex items-center gap-1 text-[11px] font-bold text-accent-600 hover:text-accent-700 uppercase tracking-wide transition-colors">
            Ver sitio en vivo
            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </a>
          <span v-else-if="project.accesoPrivado"
                class="inline-flex items-center gap-1 text-[11px] font-semibold text-ink/60 uppercase tracking-wide">
            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 .828-.672 1.5-1.5 1.5S9 11.828 9 11s.672-1.5 1.5-1.5S12 10.172 12 11zm0 0v3m-6-3V7a4 4 0 118 0v4m-9 0h10a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6a1 1 0 011-1z"/></svg>
            Acceso privado · sistema interno del negocio
          </span>
          <span class="text-[11px] font-semibold text-ink/50 uppercase tracking-wide">Maqueta referencial</span>
        </div>
      </div>
      <div class="rounded-lg border border-ink/10 bg-white overflow-hidden shadow-sm">
        <div class="flex items-center gap-2 px-3 py-2 bg-ink/[0.03] border-b border-ink/10">
          <span class="w-1.5 h-1.5 rounded-full bg-accent-500"></span>
          <span class="text-[11px] text-ink/50 font-mono">maqueta — datos de ejemplo</span>
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
