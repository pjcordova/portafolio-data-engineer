<script setup lang="ts">
const stats = [
  { value: '4', label: 'Proyectos en producción' },
  { value: '2', label: 'Países: Perú y Argentina' },
  { value: '100%', label: 'Código a medida, sin plantillas' },
];
</script>

<template>
  <section class="reveal py-12 bg-paper border-b border-ink/10">
    <div class="max-w-4xl mx-auto px-6 grid grid-cols-3 divide-x divide-ink/10 text-center">
      <div v-for="stat in stats" :key="stat.label" class="px-4">
        <div class="text-4xl md:text-5xl font-bold text-accent-600">{{ stat.value }}</div>
        <div class="text-[11px] md:text-xs font-semibold text-ink/50 uppercase tracking-wide mt-2 leading-relaxed">
          {{ stat.label }}
        </div>
      </div>
    </div>
  </section>
</template>
