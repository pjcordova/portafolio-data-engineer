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
  <section id="contacto" class="reveal py-14 bg-ink">
    <div class="max-w-2xl mx-auto px-6">
      <div class="text-center mb-8">
        <h2 class="text-sm font-bold tracking-[0.2em] text-paper/50 uppercase mb-3">Hablemos</h2>
        <h3 class="text-2xl md:text-3xl font-bold text-paper">
          Cuéntame de <span class="font-serif italic text-gold-light font-normal">tu proyecto</span>
        </h3>
      </div>

      <form class="space-y-4" @submit.prevent="handleSubmit">
        <div class="grid sm:grid-cols-2 gap-4">
          <div>
            <label for="contact-name" class="block text-xs font-bold text-paper/70 mb-1.5">Nombre</label>
            <input id="contact-name" v-model="name" type="text" required
                   class="w-full px-3.5 py-2.5 bg-paper border border-paper/20 rounded-lg text-ink placeholder:text-ink/30 focus:outline-none focus:border-gold-light transition-colors"
                   placeholder="Tu nombre" />
          </div>
          <div>
            <label for="contact-email" class="block text-xs font-bold text-paper/70 mb-1.5">Correo</label>
            <input id="contact-email" v-model="email" type="email" required
                   class="w-full px-3.5 py-2.5 bg-paper border border-paper/20 rounded-lg text-ink placeholder:text-ink/30 focus:outline-none focus:border-gold-light transition-colors"
                   placeholder="tu@correo.com" />
          </div>
        </div>
        <div>
          <label for="contact-message" class="block text-xs font-bold text-paper/70 mb-1.5">Mensaje</label>
          <textarea id="contact-message" v-model="message" required rows="3"
                    class="w-full px-3.5 py-2.5 bg-paper border border-paper/20 rounded-lg text-ink placeholder:text-ink/30 focus:outline-none focus:border-gold-light transition-colors resize-none"
                    placeholder="Cuéntame qué necesitas resolver..."></textarea>
        </div>

        <button type="submit"
                class="btn-press w-full px-8 py-3 bg-gold text-ink rounded-lg font-bold shadow-lg shadow-ink/20 hover:bg-gold-light transition-colors">
          Enviar mensaje
        </button>

        <p v-if="sent" class="text-center text-sm text-paper/50">
          Se abrió tu cliente de correo con el mensaje listo — solo dale enviar.
        </p>
      </form>
    </div>
  </section>
</template>
