<script setup lang="ts">
import { ref } from 'vue';
import { projects } from '../data/projects';
import ProjectGalleryCard from '../components/ProjectGalleryCard.vue';
import SiteNav from '../components/SiteNav.vue';
import SiteFooter from '../components/SiteFooter.vue';
import TechStack from '../components/TechStack.vue';
import AboutMe from '../components/AboutMe.vue';
import FaqSection from '../components/FaqSection.vue';
import StatsStrip from '../components/StatsStrip.vue';
import ContactForm from '../components/ContactForm.vue';
import TestimoniosSection from '../components/TestimoniosSection.vue';
import { useReveal } from '../composables/useReveal';

useReveal();

// Drop a photo at public/piero.jpg and it replaces the placeholder automatically.
// (bound via :src, not a literal template string, so Vite doesn't try to
// resolve it as a build-time import before the file exists)
const photoSrc = '/piero.jpg';
const photoMissing = ref(false);
</script>

<template>
  <SiteNav />

  <!-- Hero Section -->
  <header class="relative pt-20 pb-32 overflow-hidden bg-ink">
    <div class="absolute -top-24 right-0 w-[560px] h-[560px] rounded-full bg-accent-500/20 blur-3xl -z-10"></div>
    <div class="absolute bottom-0 left-0 w-[420px] h-[420px] rounded-full bg-gold/10 blur-3xl -z-10"></div>

    <div class="max-w-7xl mx-auto px-6 relative z-10">
      <div class="grid lg:grid-cols-[1fr_360px] gap-12 lg:gap-16 items-center">
        <div class="max-w-3xl">
          <p class="animate-fade-up text-xs font-bold tracking-[0.25em] text-accent-300 uppercase mb-6">
            Desarrollo Full Stack · B2B
          </p>
          <h1 class="animate-fade-up [animation-delay:90ms] text-5xl md:text-7xl font-bold tracking-tight text-paper leading-[1.1] mb-8">
            Transformo procesos complejos en <span class="font-serif italic text-accent-300 font-normal">soluciones digitales</span> rentables.
          </h1>
          <p class="animate-fade-up [animation-delay:180ms] text-xl md:text-2xl text-paper/60 mb-10 leading-relaxed font-light">
            Cordova Solutions | Desarrollo Full Stack Especializado en E-commerce, ERPs y Soluciones Cloud.
          </p>
          <div class="animate-fade-up [animation-delay:270ms] flex flex-wrap gap-4">
            <a href="#proyectos"
               class="btn-press group px-8 py-4 bg-accent-500 text-paper rounded-lg font-bold shadow-lg shadow-accent-500/30 hover:bg-accent-300 hover:shadow-accent-300/40 transition-colors inline-flex items-center gap-2">
              Ver Casos de Éxito
              <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
            <a href="#contacto"
               class="btn-press px-8 py-4 bg-transparent text-paper border-2 border-paper/60 rounded-lg font-bold hover:bg-paper hover:text-ink transition-colors">
              Hablemos de tu Proyecto
            </a>
          </div>
        </div>

        <!-- Photo frame: drop an image at public/piero.jpg to replace the placeholder -->
        <div class="animate-fade-up [animation-delay:150ms] relative aspect-[4/5] w-full max-w-sm mx-auto lg:max-w-none rounded-3xl overflow-hidden border border-paper/10 bg-gradient-to-br from-accent-700/40 via-ink to-gold-dark/30 shadow-xl shadow-ink/40">
          <img v-show="!photoMissing" :src="photoSrc" alt="Piero Cordova"
               class="absolute inset-0 w-full h-full object-cover"
               @error="photoMissing = true" @load="photoMissing = false" />
          <div v-if="photoMissing" class="absolute inset-0 flex flex-col items-center justify-center gap-3 text-paper/30">
            <svg class="w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
            <span class="text-xs font-bold uppercase tracking-widest">Tu foto aquí</span>
          </div>
        </div>
      </div>
    </div>
  </header>

  <AboutMe />

  <StatsStrip />

  <TechStack />

  <!-- Success Cases Section -->
  <section id="proyectos" class="py-24 bg-paper">
    <div class="max-w-7xl mx-auto px-6">
      <div class="reveal mb-16 flex flex-wrap justify-between items-end gap-6">
        <div class="max-w-2xl">
          <h2 class="text-sm font-bold tracking-[0.2em] text-accent-600 uppercase mb-4">Portafolio</h2>
          <h3 class="text-3xl md:text-4xl font-bold text-ink">Casos de Éxito & Proyectos Destacados</h3>
        </div>
      </div>

      <div v-if="projects.length === 0" class="text-center py-20 bg-ink/[0.03] rounded-2xl border border-dashed border-ink/15">
        <p class="text-ink/50">No se encontraron proyectos disponibles.</p>
      </div>

      <div v-else class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
        <div v-for="project in projects" :key="project.slug" class="reveal">
          <ProjectGalleryCard :project="project" />
        </div>
      </div>
    </div>
  </section>

  <div class="h-2 bg-gradient-to-r from-gold-dark via-gold-light to-gold-dark"></div>

  <FaqSection />

  <TestimoniosSection />

  <ContactForm />

  <!-- Methodology Section -->
  <section id="metodologia" class="py-24 bg-gold">
    <div class="max-w-7xl mx-auto px-6">
      <div class="reveal mb-16">
        <h2 class="inline-block text-base font-bold tracking-[0.15em] text-ink uppercase mb-4 px-4 py-1.5 bg-paper rounded-full shadow-sm">Metodología B2B</h2>
        <h3 class="text-3xl md:text-4xl font-bold text-paper">Enfoque estratégico para resultados tangibles</h3>
      </div>

      <div class="grid md:grid-cols-3 gap-px bg-ink/10 rounded-2xl overflow-hidden border border-ink/10 shadow-xl shadow-ink/10">
        <div class="reveal group bg-paper p-10 hover:bg-white transition-colors">
          <span class="font-serif italic text-4xl text-ink/50 group-hover:text-accent-700 transition-colors">01</span>
          <h4 class="text-xl font-bold mt-4 mb-3">Arquitectura y Diseño</h4>
          <p class="text-ink/60">Prototipado en Figma centrado en la conversión y la experiencia del usuario final.</p>
        </div>

        <div class="reveal group bg-paper p-10 hover:bg-white transition-colors [transition-delay:80ms]">
          <span class="font-serif italic text-4xl text-ink/50 group-hover:text-accent-700 transition-colors">02</span>
          <h4 class="text-xl font-bold mt-4 mb-3">Desarrollo Ágil</h4>
          <p class="text-ink/60">Stack moderno y seguro para máxima eficiencia en el procesamiento y escalabilidad.</p>
        </div>

        <div class="reveal group bg-paper p-10 hover:bg-white transition-colors [transition-delay:160ms]">
          <span class="font-serif italic text-4xl text-ink/50 group-hover:text-accent-700 transition-colors">03</span>
          <h4 class="text-xl font-bold mt-4 mb-3">Desarrollo Cloud</h4>
          <p class="text-ink/60">Alojamiento en Vercel con monitoreo 24/7 y despliegue continuo (CI/CD).</p>
        </div>
      </div>
    </div>
  </section>

  <SiteFooter />
</template>
