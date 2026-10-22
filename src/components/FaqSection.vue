<script setup lang="ts">
import { ref } from 'vue';

const faqs = [
  {
    q: '¿Cómo cotizas un proyecto?',
    a: 'Cotizo por proyecto, no por hora suelta. Primero entiendo qué necesitas resolver, estimo cuántos días me va a tomar según la complejidad, y te paso una cotización clara antes de empezar — sin sorpresas a mitad de camino.',
  },
  {
    q: '¿Qué pasa después de que entregas el proyecto?',
    a: 'Si quieres que me quede disponible de forma continua — monitoreo, ajustes, acompañamiento — lo manejamos con un pago mensual de soporte. Si más adelante necesitas un cambio puntual o una funcionalidad nueva, se cotiza aparte según qué tan compleja sea esa actualización.',
  },
  {
    q: '¿Trabajas solo o con un equipo?',
    a: 'Por ahora trabajo solo. Hablas directo conmigo de principio a fin — no hay un project manager de por medio ni el código pasa por manos que no conozco.',
  },
  {
    q: '¿Solo trabajas con empresas en Perú?',
    a: 'No. Soy de Lima, Perú, y atiendo presencial a clientes de acá — pero también trabajo remoto con empresas de toda Latinoamérica. Ahora mismo, por ejemplo, desarrollo el sitio web de Buenvivir, una consultora en Argentina.',
  },
  {
    q: '¿Qué pasa si no sé exactamente qué necesito?',
    a: 'Pasa seguido. Nos sentamos, conversamos sobre cómo funciona tu negocio hoy, y de ahí te ayudo a traducir eso en una solución concreta. No necesitas llegar con un documento técnico, solo con el problema que quieres resolver.',
  },
];

const openIndex = ref<number | null>(0);

function toggle(i: number) {
  openIndex.value = openIndex.value === i ? null : i;
}
</script>

<template>
  <section id="faq" class="reveal py-14 bg-accent-700">
    <div class="max-w-3xl mx-auto px-6">
      <div class="text-center mb-8">
        <div class="inline-block bg-paper rounded-2xl px-7 py-4 shadow-xl shadow-ink/20">
          <h2 class="text-xs font-bold tracking-[0.2em] text-accent-600 uppercase mb-2">Preguntas Frecuentes</h2>
          <h3 class="text-2xl md:text-3xl font-bold text-ink">
            Antes de <span class="font-serif italic text-accent-600 font-normal">escribirme</span>
          </h3>
        </div>
      </div>

      <div class="divide-y divide-paper/10 border-y border-paper/10">
        <div v-for="(item, i) in faqs" :key="item.q">
          <button type="button"
                  class="w-full flex items-center justify-between gap-4 py-4 text-left"
                  :aria-expanded="openIndex === i"
                  @click="toggle(i)">
            <span class="text-sm font-bold text-paper">{{ item.q }}</span>
            <svg class="w-4 h-4 flex-shrink-0 text-paper/40 transition-transform duration-200 ease-[cubic-bezier(0.16,1,0.3,1)]"
                 :class="openIndex === i ? 'rotate-45' : ''"
                 fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
            </svg>
          </button>
          <div class="grid transition-[grid-template-rows] duration-[250ms] ease-[cubic-bezier(0.16,1,0.3,1)] faq-panel"
               :style="{ gridTemplateRows: openIndex === i ? '1fr' : '0fr' }">
            <div class="overflow-hidden">
              <p class="text-sm text-paper/60 leading-relaxed pb-4 pr-8">{{ item.a }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (prefers-reduced-motion: reduce) {
  .faq-panel {
    transition: none;
  }
}
</style>
