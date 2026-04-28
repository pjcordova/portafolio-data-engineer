<script setup lang="ts">
interface Project {
  nombre: string;
  cliente: string;
  categoria_solucion: string;
  problema_resuelto: string;
  metrica_impacto: string;
  tecnologias: string[];
  status: string;
  link_demo?: string;
  link_figma?: string;
}

defineProps<{
  project: Project;
}>();
</script>

<template>
  <div class="group bg-white border border-slate-200 rounded-xl overflow-hidden hover:shadow-xl transition-all duration-300 flex flex-col md:flex-row">
    <!-- Visual Accent Side -->
    <div class="w-full md:w-2 bg-slate-900 group-hover:bg-blue-600 transition-colors"></div>
    
    <div class="p-8 flex-1">
      <div class="flex flex-wrap justify-between items-start mb-4 gap-4">
        <div>
          <span class="text-xs font-bold tracking-widest text-slate-400 uppercase">{{ project.categoria_solucion }}</span>
          <h3 class="text-2xl font-bold text-slate-900 mt-1">{{ project.nombre }}</h3>
          <p v-if="project.cliente" class="text-slate-500 font-medium">Cliente: {{ project.cliente }}</p>
        </div>
        <div class="flex gap-2">
          <span v-if="project.status" 
                class="px-3 py-1 rounded-full text-xs font-semibold"
                :class="project.status === 'Completado' ? 'bg-green-50 text-green-700 border border-green-200' : 'bg-amber-50 text-amber-700 border border-amber-200'">
            {{ project.status }}
          </span>
        </div>
      </div>

      <div class="grid md:grid-cols-2 gap-8 mb-6">
        <div>
          <h4 class="text-sm font-bold text-slate-900 uppercase tracking-wider mb-2">Problema Resuelto</h4>
          <p class="text-slate-600 leading-relaxed">{{ project.problema_resuelto }}</p>
        </div>
        <div v-if="project.metrica_impacto" class="bg-slate-50 p-4 rounded-lg border border-slate-100">
          <h4 class="text-sm font-bold text-slate-900 uppercase tracking-wider mb-2">Métrica de Impacto</h4>
          <p class="text-blue-900 font-semibold text-lg">{{ project.metrica_impacto }}</p>
        </div>
      </div>

      <div class="flex flex-wrap gap-2 mb-8">
        <span v-for="tech in project.tecnologias" :key="tech" 
              class="px-2.5 py-1 bg-slate-100 text-slate-700 text-xs font-medium rounded border border-slate-200">
          {{ tech }}
        </span>
      </div>

      <div class="flex flex-wrap gap-4 pt-6 border-t border-slate-100">
        <a v-if="project.link_demo" :href="project.link_demo" target="_blank" 
           class="inline-flex items-center text-sm font-bold text-slate-900 hover:text-blue-600 transition-colors">
          Explorar Solución
          <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
        <a v-if="project.link_figma" :href="project.link_figma" target="_blank" 
           class="inline-flex items-center text-sm font-bold text-slate-500 hover:text-slate-900 transition-colors">
          Diseño en Figma
          <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
        </a>
      </div>
    </div>
  </div>
</template>
