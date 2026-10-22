<script setup lang="ts">
import { ref } from 'vue';

// Drop a photo at public/piero-about.jpg and it replaces the placeholder automatically.
const photoSrc = '/piero-about.jpg';
const photoMissing = ref(false);
</script>

<template>
  <section id="sobre-mi" class="py-14 bg-paper">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid lg:grid-cols-[260px_1fr] gap-10 lg:gap-12 items-center">
        <div class="reveal relative aspect-[4/5] w-full max-w-[260px] mx-auto rounded-3xl overflow-hidden border border-ink/10 bg-gradient-to-br from-accent-50 via-paper to-gold/10 shadow-xl shadow-ink/5">
          <img v-show="!photoMissing" :src="photoSrc" alt="Piero Cordova"
               class="absolute inset-0 w-full h-full object-cover"
               @error="photoMissing = true" @load="photoMissing = false" />
          <div v-if="photoMissing" class="absolute inset-0 flex flex-col items-center justify-center gap-3 text-ink/25">
            <svg class="w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
            <span class="text-xs font-bold uppercase tracking-widest">Tu foto aquí</span>
          </div>
        </div>

        <div class="reveal">
          <h2 class="text-xs font-bold tracking-[0.2em] text-accent-600 uppercase mb-2">Sobre Mí</h2>
          <h3 class="text-2xl md:text-3xl font-bold text-ink mb-4 leading-tight">
            Software que se adapta a <span class="font-serif italic text-accent-600 font-normal">tu negocio</span>, no al revés.
          </h3>
          <div class="space-y-3 text-sm text-ink/60 leading-relaxed mb-6 max-w-2xl">
            <p>
              Soy Piero Cordova, fundador de Cordova Solutions. Empecé a programar en la universidad
              — desde quinto ciclo ya estaba metido en proyectos reales — y hoy, en décimo ciclo, los
              sistemas que he construido ya los usan empresas de verdad: Chavely ERP ordena las finanzas
              diarias de un negocio físico, Bithia Web vende en línea, AIB+ la acabo de lanzar como
              plataforma de servicios, y el sitio de Buen Vivir conecta a una consultora regenerativa
              de Argentina con clientes de toda Latinoamérica.
            </p>
            <p>
              No desarrollo por desarrollar. Para mí un sistema solo sirve si resuelve el proceso real
              de tu negocio, y solo es bueno si tu equipo puede aprenderlo rápido sin dejar de ser
              eficiente en el día a día. Por eso me involucro de cerca con cada cliente antes de escribir
              una sola línea de código — y prefiero ser claro con los tiempos desde el inicio: no todos
              los proyectos toman lo mismo.
            </p>
          </div>

          <div class="grid sm:grid-cols-3 gap-4">
            <div>
              <span class="font-serif italic text-xl text-accent-600">01</span>
              <p class="text-sm font-bold text-ink mt-1 mb-0.5">Cercanía real</p>
              <p class="text-xs text-ink/50 leading-relaxed">Hablas directo conmigo, no con un intermediario.</p>
            </div>
            <div>
              <span class="font-serif italic text-xl text-accent-600">02</span>
              <p class="text-sm font-bold text-ink mt-1 mb-0.5">Procesos primero</p>
              <p class="text-xs text-ink/50 leading-relaxed">Si no encaja con cómo trabaja tu empresa, no sirve.</p>
            </div>
            <div>
              <span class="font-serif italic text-xl text-accent-600">03</span>
              <p class="text-sm font-bold text-ink mt-1 mb-0.5">Fácil de usar</p>
              <p class="text-xs text-ink/50 leading-relaxed">Curva de aprendizaje baja, eficiente en el trabajo diario.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
