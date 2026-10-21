<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { projects } from './data/projects';
import ProjectCard from './components/ProjectCard.vue';

const menuOpen = ref(false);

onMounted(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
  );
  document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
});
</script>

<template>
  <div class="min-h-screen bg-paper text-ink font-sans">
    <!-- Navigation -->
    <nav class="sticky top-0 z-50 bg-paper/80 backdrop-blur-md border-b border-ink/10">
      <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        <div class="text-xl font-bold tracking-tighter text-ink">
          CORDOVA SOLUTIONS<span class="text-accent-600">.</span>
        </div>
        <div class="hidden md:flex gap-8 text-sm font-medium">
          <a href="#metodologia" class="nav-link">Metodología</a>
          <a href="#proyectos" class="nav-link">Casos de Éxito</a>
          <a href="#contacto" class="nav-link">Contacto</a>
        </div>
        <button
          class="md:hidden w-8 h-8 flex flex-col items-center justify-center gap-[5px]"
          aria-label="Abrir menú"
          :aria-expanded="menuOpen"
          @click="menuOpen = !menuOpen">
          <span class="block w-6 h-[1.5px] bg-ink transition-transform duration-300 origin-center"
                :class="menuOpen ? 'rotate-45 translate-y-[3px]' : ''"></span>
          <span class="block w-6 h-[1.5px] bg-ink transition-transform duration-300 origin-center"
                :class="menuOpen ? '-rotate-45 -translate-y-[3px]' : ''"></span>
        </button>
      </div>
      <div v-show="menuOpen" class="md:hidden border-t border-ink/10 bg-paper px-6 py-4 flex flex-col gap-4 text-sm font-medium">
        <a href="#metodologia" class="nav-link" @click="menuOpen = false">Metodología</a>
        <a href="#proyectos" class="nav-link" @click="menuOpen = false">Casos de Éxito</a>
        <a href="#contacto" class="nav-link" @click="menuOpen = false">Contacto</a>
      </div>
    </nav>

    <!-- Hero Section -->
    <header class="relative pt-20 pb-32 overflow-hidden">
      <div class="absolute -top-24 right-0 w-[560px] h-[560px] rounded-full bg-accent-100/70 blur-3xl -z-10"></div>

      <div class="max-w-7xl mx-auto px-6 relative z-10">
        <div class="max-w-3xl">
          <p class="animate-fade-up text-xs font-bold tracking-[0.25em] text-accent-600 uppercase mb-6">
            Desarrollo Full Stack · B2B
          </p>
          <h1 class="animate-fade-up [animation-delay:90ms] text-5xl md:text-7xl font-bold tracking-tight text-ink leading-[1.1] mb-8">
            Transformo procesos complejos en <span class="font-serif italic text-accent-600 font-normal">soluciones digitales</span> rentables.
          </h1>
          <p class="animate-fade-up [animation-delay:180ms] text-xl md:text-2xl text-ink/50 mb-10 leading-relaxed font-light">
            Cordova Solutions | Desarrollo Full Stack Especializado en E-commerce, ERPs y Soluciones Cloud.
          </p>
          <div class="animate-fade-up [animation-delay:270ms] flex flex-wrap gap-4">
            <a href="#proyectos"
               class="btn-press group px-8 py-4 bg-ink text-paper rounded-lg font-bold shadow-lg shadow-ink/10 hover:shadow-xl hover:shadow-ink/15 transition-shadow inline-flex items-center gap-2">
              Ver Casos de Éxito
              <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
            <a href="#contacto"
               class="btn-press px-8 py-4 bg-transparent text-ink border-2 border-ink/15 rounded-lg font-bold hover:border-ink/40 transition-colors">
              Hablemos de tu Proyecto
            </a>
          </div>
        </div>
      </div>
    </header>

    <!-- Methodology Section -->
    <section id="metodologia" class="py-24 bg-ink/[0.03]">
      <div class="max-w-7xl mx-auto px-6">
        <div class="reveal mb-16">
          <h2 class="text-sm font-bold tracking-[0.2em] text-accent-600 uppercase mb-4">Metodología B2B</h2>
          <h3 class="text-3xl md:text-4xl font-bold text-ink">Enfoque estratégico para resultados tangibles</h3>
        </div>

        <div class="grid md:grid-cols-3 gap-px bg-ink/10 rounded-2xl overflow-hidden border border-ink/10">
          <div class="reveal group bg-paper p-10 hover:bg-white transition-colors">
            <span class="font-serif italic text-4xl text-accent-600/40 group-hover:text-accent-600 transition-colors">01</span>
            <h4 class="text-xl font-bold mt-4 mb-3">Arquitectura y Diseño</h4>
            <p class="text-ink/60">Prototipado en Figma centrado en la conversión y la experiencia del usuario final.</p>
          </div>

          <div class="reveal group bg-paper p-10 hover:bg-white transition-colors [transition-delay:80ms]">
            <span class="font-serif italic text-4xl text-accent-600/40 group-hover:text-accent-600 transition-colors">02</span>
            <h4 class="text-xl font-bold mt-4 mb-3">Desarrollo Ágil</h4>
            <p class="text-ink/60">Stack moderno y seguro para máxima eficiencia en el procesamiento y escalabilidad.</p>
          </div>

          <div class="reveal group bg-paper p-10 hover:bg-white transition-colors [transition-delay:160ms]">
            <span class="font-serif italic text-4xl text-accent-600/40 group-hover:text-accent-600 transition-colors">03</span>
            <h4 class="text-xl font-bold mt-4 mb-3">Desarrollo Cloud</h4>
            <p class="text-ink/60">Alojamiento en Vercel con monitoreo 24/7 y despliegue continuo (CI/CD).</p>
          </div>
        </div>
      </div>
    </section>

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

        <div v-else class="space-y-12">
          <div v-for="project in projects" :key="project.slug" class="reveal">
            <ProjectCard :project="project" />
          </div>
        </div>
      </div>
    </section>

    <!-- Footer / Contact -->
    <footer id="contacto" class="bg-ink text-paper py-24">
      <div class="max-w-7xl mx-auto px-6">
        <div class="reveal grid md:grid-cols-2 gap-16 items-start">
          <div>
            <h2 class="text-4xl font-serif italic font-normal mb-8">¿Listo para escalar tu infraestructura digital?</h2>
            <p class="text-paper/50 text-lg mb-12">
              Analicemos cómo mis habilidades en desarrollo Full Stack y arquitectura de datos pueden beneficiar a tu empresa.
            </p>
            <div class="space-y-6">
              <div class="flex items-center gap-4">
                <div class="w-10 h-10 bg-paper/10 rounded-full flex items-center justify-center">
                  <svg class="w-5 h-5 text-accent-500" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79a15.15 15.15 0 006.59 6.59l2.2-2.2a1 1 0 011.11-.27 11.72 11.72 0 003.7 0.59 1 1 0 011 1V20a1 1 0 01-1 1A15 15 0 013 6a1 1 0 011-1h3.41a1 1 0 011 1 11.72 11.72 0 000.59 3.7 1 1 0 01-.27 1.11l-2.2 2.2z"/></svg>
                </div>
                <span>+51 967 601 604</span>
              </div>
              <div class="flex items-center gap-4">
                <div class="w-10 h-10 bg-paper/10 rounded-full flex items-center justify-center">
                  <svg class="w-5 h-5 text-accent-500" fill="currentColor" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                </div>
                <span>cordova23piero@gmail.com</span>
              </div>
              <div class="flex items-center gap-4">
                <div class="w-10 h-10 bg-paper/10 rounded-full flex items-center justify-center">
                  <svg class="w-5 h-5 text-accent-500" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z"/></svg>
                </div>
                <span>Ica, Perú</span>
              </div>
            </div>
          </div>

          <div class="bg-paper/5 p-10 rounded-2xl border border-paper/10">
            <h3 class="text-2xl font-bold mb-6">Redes Profesionales</h3>
            <div class="flex gap-4">
              <a href="https://github.com/pjcordova" target="_blank"
                 class="btn-press px-6 py-3 bg-paper text-ink rounded-lg font-bold hover:bg-paper/90 transition-colors">
                GitHub
              </a>
              <a href="https://www.linkedin.com/in/piero-cordova-cerna-5a9886318/" class="btn-press px-6 py-3 bg-accent-600 text-paper rounded-lg font-bold hover:bg-accent-700 transition-colors">
                LinkedIn
              </a>
            </div>
          </div>
        </div>

        <div class="mt-20 pt-8 border-t border-paper/10 text-center text-paper/40 text-sm">
          <p>© 2026 Cordova Solutions. Todos los derechos reservados.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Instrument+Serif:ital@1&display=swap');

html {
  scroll-behavior: smooth;
}

body {
  font-family: 'Inter', sans-serif;
}

.nav-link {
  position: relative;
  color: #131210;
  transition: color 0.2s ease;
}
.nav-link::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -4px;
  width: 100%;
  height: 1.5px;
  background: #2F5BFF;
  transform: scaleX(0);
  transform-origin: right;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.nav-link:hover {
  color: #2F5BFF;
}
.nav-link:hover::after {
  transform: scaleX(1);
  transform-origin: left;
}

.btn-press {
  transition: transform 0.15s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s ease, background-color 0.2s ease, border-color 0.2s ease;
}
.btn-press:active {
  transform: scale(0.97);
}
</style>
