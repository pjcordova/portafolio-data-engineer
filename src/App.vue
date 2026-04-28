<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { supabase } from './lib/supabase';
import ProjectCard from './components/ProjectCard.vue';

const projects = ref<any[]>([]);
const loading = ref(true);

const fetchProjects = async () => {
  try {
    loading.value = true;
    const { data, error } = await supabase
      .from('proyectos')
      .select('nombre, cliente, categoria_solucion, problema_resuelto, metrica_impacto, tecnologias, status, link_demo, link_figma');

    if (error) throw error;
    projects.value = data || [];
  } catch (error) {
    console.error('Error fetching projects:', error);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchProjects();
});
</script>

<template>
  <div class="min-h-screen bg-[#FFFFFF] text-[#1E293B] font-sans selection:bg-slate-900 selection:text-white">
    <!-- Navigation -->
    <nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-100">
      <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        <div class="text-xl font-bold tracking-tighter text-[#0F172A]">
          PIERO CORDOVA<span class="text-blue-600">.</span>
        </div>
        <div class="hidden md:flex gap-8 text-sm font-medium">
          <a href="#metodologia" class="hover:text-blue-600 transition-colors">Metodología</a>
          <a href="#proyectos" class="hover:text-blue-600 transition-colors">Casos de Éxito</a>
          <a href="#contacto" class="hover:text-blue-600 transition-colors">Contacto</a>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <header class="relative pt-20 pb-32 overflow-hidden">
      <div class="max-w-7xl mx-auto px-6 relative z-10">
        <div class="max-w-3xl">
          <h1 class="text-5xl md:text-7xl font-bold tracking-tight text-[#0F172A] leading-[1.1] mb-8">
            Transformo procesos complejos en <span class="text-blue-600">soluciones digitales</span> rentables.
          </h1>
          <p class="text-xl md:text-2xl text-slate-500 mb-10 leading-relaxed font-light">
            Ing. Piero Cordova | Desarrollador Full Stack Especializado en E-commerce, ERPs y Soluciones Cloud.
          </p>
          <div class="flex flex-wrap gap-4">
            <a href="#proyectos" 
               class="px-8 py-4 bg-[#0F172A] text-white rounded-lg font-bold hover:bg-slate-800 transition-all transform hover:-translate-y-1 shadow-lg">
              Ver Casos de Éxito
            </a>
            <a href="#contacto" 
               class="px-8 py-4 bg-white text-[#0F172A] border-2 border-slate-200 rounded-lg font-bold hover:border-slate-900 transition-all">
              Hablemos de tu Proyecto
            </a>
          </div>
        </div>
      </div>
      <!-- Subtle Background Decor -->
      <div class="absolute top-0 right-0 w-1/2 h-full bg-slate-50 -z-10 skew-x-12 translate-x-1/4"></div>
    </header>

    <!-- Methodology Section -->
    <section id="metodologia" class="py-24 bg-[#F8FAFC]">
      <div class="max-w-7xl mx-auto px-6">
        <div class="mb-16">
          <h2 class="text-sm font-bold tracking-[0.2em] text-blue-600 uppercase mb-4">Metodología B2B</h2>
          <h3 class="text-3xl md:text-4xl font-bold text-[#0F172A]">Enfoque estratégico para resultados tangibles</h3>
        </div>
        
        <div class="grid md:grid-cols-3 gap-12">
          <div class="bg-white p-10 rounded-2xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
            <div class="w-12 h-12 bg-blue-50 rounded-lg flex items-center justify-center mb-6 text-blue-600">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
            </div>
            <h4 class="text-xl font-bold mb-4">Arquitectura y Diseño</h4>
            <p class="text-slate-600">Prototipado en Figma centrado en la conversión y la experiencia del usuario final.</p>
          </div>

          <div class="bg-white p-10 rounded-2xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
            <div class="w-12 h-12 bg-slate-100 rounded-lg flex items-center justify-center mb-6 text-slate-900">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
            </div>
            <h4 class="text-xl font-bold mb-4">Desarrollo Ágil</h4>
            <p class="text-slate-600">Stack moderno y seguro para máxima eficiencia en el procesamiento y escalabilidad.</p>
          </div>

          <div class="bg-white p-10 rounded-2xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
            <div class="w-12 h-12 bg-blue-50 rounded-lg flex items-center justify-center mb-6 text-blue-600">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01"/></svg>
            </div>
            <h4 class="text-xl font-bold mb-4">Desarrollo Cloud</h4>
            <p class="text-slate-600">Alojamiento en Vercel con monitoreo 24/7 y despliegue continuo (CI/CD).</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Success Cases Section -->
    <section id="proyectos" class="py-24 bg-white">
      <div class="max-w-7xl mx-auto px-6">
        <div class="mb-16 flex flex-wrap justify-between items-end gap-6">
          <div class="max-w-2xl">
            <h2 class="text-sm font-bold tracking-[0.2em] text-blue-600 uppercase mb-4">Portafolio</h2>
            <h3 class="text-3xl md:text-4xl font-bold text-[#0F172A]">Casos de Éxito & Proyectos Destacados</h3>
          </div>
        </div>

        <div v-if="loading" class="flex justify-center py-20">
          <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-slate-900"></div>
        </div>

        <div v-else-if="projects.length === 0" class="text-center py-20 bg-slate-50 rounded-2xl border border-dashed border-slate-200">
          <p class="text-slate-500">No se encontraron proyectos disponibles.</p>
        </div>

        <div v-else class="space-y-12">
          <ProjectCard v-for="project in projects" :key="project.nombre" :project="project" />
        </div>
      </div>
    </section>

    <!-- Footer / Contact -->
    <footer id="contacto" class="bg-[#0F172A] text-white py-24">
      <div class="max-w-7xl mx-auto px-6">
        <div class="grid md:grid-cols-2 gap-16 items-start">
          <div>
            <h2 class="text-4xl font-bold mb-8 italic">¿Listo para escalar tu infraestructura digital?</h2>
            <p class="text-slate-400 text-lg mb-12">
              Analicemos cómo mis habilidades en desarrollo Full Stack y arquitectura de datos pueden beneficiar a tu empresa.
            </p>
            <div class="space-y-6">
              <div class="flex items-center gap-4">
                <div class="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center">
                  <svg class="w-5 h-5 text-blue-400" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79a15.15 15.15 0 006.59 6.59l2.2-2.2a1 1 0 011.11-.27 11.72 11.72 0 003.7 0.59 1 1 0 011 1V20a1 1 0 01-1 1A15 15 0 013 6a1 1 0 011-1h3.41a1 1 0 011 1 11.72 11.72 0 000.59 3.7 1 1 0 01-.27 1.11l-2.2 2.2z"/></svg>
                </div>
                <span>+51 967 601 604</span>
              </div>
              <div class="flex items-center gap-4">
                <div class="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center">
                  <svg class="w-5 h-5 text-blue-400" fill="currentColor" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                </div>
                <span>cordova23piero@gmail.com</span>
              </div>
              <div class="flex items-center gap-4">
                <div class="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center">
                  <svg class="w-5 h-5 text-blue-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z"/></svg>
                </div>
                <span>Ica, Perú</span>
              </div>
            </div>
          </div>
          
          <div class="bg-slate-800/50 p-10 rounded-2xl border border-slate-700">
            <h3 class="text-2xl font-bold mb-6">Redes Profesionales</h3>
            <div class="flex gap-4">
              <a href="https://github.com/pjcordova" target="_blank" 
                 class="px-6 py-3 bg-white text-[#0F172A] rounded-lg font-bold hover:bg-slate-100 transition-colors">
                GitHub
              </a>
              <a href="https://www.linkedin.com/in/piero-cordova-cerna-5a9886318/" class="px-6 py-3 bg-blue-600 text-white rounded-lg font-bold hover:bg-blue-700 transition-colors">
                LinkedIn
              </a>
            </div>
          </div>
        </div>
        
        <div class="mt-20 pt-8 border-t border-slate-800 text-center text-slate-500 text-sm">
          <p>© 2026 Ing. Piero Cordova. Todos los derechos reservados.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html {
  scroll-behavior: smooth;
}

body {
  font-family: 'Inter', sans-serif;
}
</style>
