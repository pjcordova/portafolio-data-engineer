<template>
  <div class="min-h-screen bg-paper text-ink font-sans">
    <RouterView />
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
