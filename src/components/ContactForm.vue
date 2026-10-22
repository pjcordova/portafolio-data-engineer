<script setup lang="ts">
import { ref } from 'vue';

const name = ref('');
const email = ref('');
const message = ref('');
const sent = ref(false);

// Hasta que el formulario esté conectado a EmailJS (o similar), arma el
// correo con lo que escribió el visitante y lo abre en su cliente de email.
function handleSubmit() {
  const subject = encodeURIComponent(`Nuevo contacto desde el portafolio — ${name.value}`);
  const body = encodeURIComponent(`Nombre: ${name.value}\nCorreo: ${email.value}\n\nMensaje:\n${message.value}`);
  window.location.href = `mailto:cordova23piero@gmail.com?subject=${subject}&body=${body}`;
  sent.value = true;
}
</script>

<template>
  <section id="contacto" class="reveal py-24 bg-paper">
    <div class="max-w-2xl mx-auto px-6">
      <div class="text-center mb-14">
        <h2 class="text-sm font-bold tracking-[0.2em] text-accent-600 uppercase mb-4">Hablemos</h2>
        <h3 class="text-3xl md:text-4xl font-bold text-ink">
          Cuéntame de <span class="font-serif italic text-accent-600 font-normal">tu proyecto</span>
        </h3>
      </div>

      <form class="space-y-5" @submit.prevent="handleSubmit">
        <div>
          <label for="contact-name" class="block text-sm font-bold text-ink mb-2">Nombre</label>
          <input id="contact-name" v-model="name" type="text" required
                 class="w-full px-4 py-3 bg-white border border-ink/15 rounded-lg text-ink placeholder:text-ink/30 focus:outline-none focus:border-accent-500 transition-colors"
                 placeholder="Tu nombre" />
        </div>
        <div>
          <label for="contact-email" class="block text-sm font-bold text-ink mb-2">Correo</label>
          <input id="contact-email" v-model="email" type="email" required
                 class="w-full px-4 py-3 bg-white border border-ink/15 rounded-lg text-ink placeholder:text-ink/30 focus:outline-none focus:border-accent-500 transition-colors"
                 placeholder="tu@correo.com" />
        </div>
        <div>
          <label for="contact-message" class="block text-sm font-bold text-ink mb-2">Mensaje</label>
          <textarea id="contact-message" v-model="message" required rows="5"
                    class="w-full px-4 py-3 bg-white border border-ink/15 rounded-lg text-ink placeholder:text-ink/30 focus:outline-none focus:border-accent-500 transition-colors resize-none"
                    placeholder="Cuéntame qué necesitas resolver..."></textarea>
        </div>

        <button type="submit"
                class="btn-press w-full px-8 py-4 bg-accent-600 text-paper rounded-lg font-bold shadow-lg shadow-accent-600/20 hover:bg-accent-700 transition-colors">
          Enviar mensaje
        </button>

        <p v-if="sent" class="text-center text-sm text-ink/50">
          Se abrió tu cliente de correo con el mensaje listo — solo dale enviar.
        </p>
      </form>
    </div>
  </section>
</template>
