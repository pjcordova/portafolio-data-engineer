<script setup lang="ts">
import { testimonios } from '../data/testimonios';
</script>

<template>
  <section v-if="testimonios.length > 0" id="testimonios" class="reveal py-24 bg-paper">
    <div class="max-w-5xl mx-auto px-6">
      <div class="text-center mb-14">
        <h2 class="text-sm font-bold tracking-[0.2em] text-accent-600 uppercase mb-4">Testimonios</h2>
        <h3 class="text-3xl md:text-4xl font-bold text-ink">
          Lo que dicen mis <span class="font-serif italic text-accent-600 font-normal">clientes</span>
        </h3>
      </div>

      <div class="grid sm:grid-cols-2 gap-6">
        <div v-for="(t, i) in testimonios" :key="i"
             class="bg-white border border-ink/10 rounded-2xl p-7 shadow-sm">
          <div class="flex gap-0.5 mb-4" :aria-label="`${t.puntuacion} de 5 estrellas`">
            <svg v-for="n in 5" :key="n" class="w-4 h-4"
                 :class="n <= t.puntuacion ? 'text-gold' : 'text-ink/15'"
                 fill="currentColor" viewBox="0 0 20 20">
              <path d="M10 1.5l2.6 5.27 5.82.85-4.21 4.1.99 5.8L10 14.9l-5.2 2.72.99-5.8-4.21-4.1 5.82-.85L10 1.5z" />
            </svg>
          </div>
          <p class="text-ink/70 leading-relaxed mb-5">"{{ t.cita }}"</p>
          <div class="text-sm">
            <span class="font-bold text-ink">{{ t.autor }}</span>
            <span class="text-ink/50"> — {{ t.cargo }}, {{ t.empresa }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
