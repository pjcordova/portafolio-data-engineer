<script setup lang="ts">
import { ref } from 'vue';

const menuOpen = ref(false);
</script>

<template>
  <nav class="fixed top-0 inset-x-0 z-50 bg-paper border-b-2 border-gold transform-gpu will-change-transform [backface-visibility:hidden]">
    <div class="h-[3px] bg-gradient-to-r from-gold-dark via-gold-light to-gold-dark"></div>
    <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
      <RouterLink to="/" class="flex items-center gap-2.5 text-xl font-bold tracking-tighter text-ink">
        <img src="/logo-icon.png" alt="" class="w-8 h-8" />
        CORDOVA SOLUTIONS<span class="text-accent-600">.</span>
      </RouterLink>
      <div class="hidden md:flex gap-8 text-sm font-medium">
        <RouterLink :to="{ path: '/', hash: '#sobre-mi' }" class="nav-link">Sobre Mí</RouterLink>
        <RouterLink :to="{ path: '/', hash: '#metodologia' }" class="nav-link">Metodología</RouterLink>
        <RouterLink :to="{ path: '/', hash: '#proyectos' }" class="nav-link">Casos de Éxito</RouterLink>
        <RouterLink :to="{ path: '/', hash: '#contacto' }" class="nav-link">Contacto</RouterLink>
      </div>
      <button
        class="md:hidden w-8 h-8 flex flex-col items-center justify-center gap-[5px]"
        aria-label="Abrir menú"
        :aria-expanded="menuOpen"
        @click="menuOpen = !menuOpen">
        <span class="block w-6 h-[1.5px] bg-ink transition-transform duration-300 ease-[cubic-bezier(0.16,1,0.3,1)] origin-center"
              :class="menuOpen ? 'rotate-45 translate-y-[3px]' : ''"></span>
        <span class="block w-6 h-[1.5px] bg-ink transition-transform duration-300 ease-[cubic-bezier(0.16,1,0.3,1)] origin-center"
              :class="menuOpen ? '-rotate-45 -translate-y-[3px]' : ''"></span>
      </button>
    </div>
    <Transition name="mobile-menu">
      <div v-show="menuOpen" class="md:hidden border-t border-ink/10 bg-paper px-6 py-4 flex flex-col gap-4 text-sm font-medium">
        <RouterLink :to="{ path: '/', hash: '#sobre-mi' }" class="nav-link" @click="menuOpen = false">Sobre Mí</RouterLink>
        <RouterLink :to="{ path: '/', hash: '#metodologia' }" class="nav-link" @click="menuOpen = false">Metodología</RouterLink>
        <RouterLink :to="{ path: '/', hash: '#proyectos' }" class="nav-link" @click="menuOpen = false">Casos de Éxito</RouterLink>
        <RouterLink :to="{ path: '/', hash: '#contacto' }" class="nav-link" @click="menuOpen = false">Contacto</RouterLink>
      </div>
    </Transition>
  </nav>
  <div class="h-[85px]" aria-hidden="true"></div>
</template>

<style scoped>
.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: opacity 200ms cubic-bezier(0.16, 1, 0.3, 1), transform 200ms cubic-bezier(0.16, 1, 0.3, 1);
}
.mobile-menu-enter-from,
.mobile-menu-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
@media (prefers-reduced-motion: reduce) {
  .mobile-menu-enter-active,
  .mobile-menu-leave-active {
    transition: none;
  }
}
</style>
