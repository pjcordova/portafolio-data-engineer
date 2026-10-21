<script setup lang="ts">
import { ref } from 'vue';

const menuOpen = ref(false);
</script>

<template>
  <nav class="sticky top-0 z-50 bg-paper/80 backdrop-blur-md border-b border-ink/10">
    <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
      <RouterLink to="/" class="text-xl font-bold tracking-tighter text-ink">
        CORDOVA SOLUTIONS<span class="text-accent-600">.</span>
      </RouterLink>
      <div class="hidden md:flex gap-8 text-sm font-medium">
        <RouterLink :to="{ path: '/', hash: '#metodologia' }" class="nav-link">Metodología</RouterLink>
        <RouterLink :to="{ path: '/', hash: '#proyectos' }" class="nav-link">Casos de Éxito</RouterLink>
        <RouterLink :to="{ path: '/', hash: '#contacto' }" class="nav-link">Contacto</RouterLink>
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
      <RouterLink :to="{ path: '/', hash: '#metodologia' }" class="nav-link" @click="menuOpen = false">Metodología</RouterLink>
      <RouterLink :to="{ path: '/', hash: '#proyectos' }" class="nav-link" @click="menuOpen = false">Casos de Éxito</RouterLink>
      <RouterLink :to="{ path: '/', hash: '#contacto' }" class="nav-link" @click="menuOpen = false">Contacto</RouterLink>
    </div>
  </nav>
</template>
