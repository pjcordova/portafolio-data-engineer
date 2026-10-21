# Cordova Solutions

![Vue](https://img.shields.io/badge/Frontend-Vue%203-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white)
![TypeScript](https://img.shields.io/badge/Lang-TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Vite](https://img.shields.io/badge/Build-Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Styles-TailwindCSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Maquetas-Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Vercel](https://img.shields.io/badge/Hosting-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

## 📋 Descripción

Sitio corporativo de **Cordova Solutions**, desarrollado en Vue 3 + Tailwind CSS, que presenta casos de éxito reales en desarrollo Full Stack, ERPs, e-commerce y soluciones cloud.

Los proyectos mostrados en la sección "Casos de Éxito" están definidos de forma estática en [`src/data/projects.ts`](./src/data/projects.ts) — no hay conexión a bases de datos ni accesos en vivo a los sistemas de los clientes. Para cada proyecto se muestra una **maqueta referencial** (HTML/CSS/Bootstrap, con datos de ejemplo) en lugar de un enlace directo a la aplicación real.

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Uso en el Proyecto |
| :--- | :--- | :--- |
| **Frontend** | Vue 3 + Vite + TypeScript | SPA con composición reactiva y tipado estático. |
| **Estilos** | Tailwind CSS | Sistema de diseño utilitario, responsive. |
| **Datos de proyectos** | TypeScript estático (`src/data/projects.ts`) | Fuente de verdad de los casos de éxito mostrados. |
| **Maquetas** | HTML + CSS + Bootstrap 5 (CDN), embebidas en `<iframe>` | Vista referencial de cada solución, sin exponer datos/accesos reales. |
| **Hosting** | Vercel | Build estático (`vite build`) con despliegue continuo. |

## 🚀 Desarrollo Local

```bash
npm install
npm run dev
```

Build de producción:

```bash
npm run build
npm run preview
```

## 🗂️ Estructura de datos (`src/data/projects.ts`)

Cada entrada representa un caso de éxito mostrado en el sitio:

| Campo | Descripción |
| :--- | :--- |
| `nombre` | Nombre del proyecto |
| `cliente` | Cliente (opcional) |
| `categoria` | Categoría (E-commerce, ERP, EdTech, etc.) |
| `problemaResuelto` | Descripción del problema que resuelve |
| `proceso` | Pasos del proceso de trabajo (descubrimiento, diseño, desarrollo, entrega) |
| `tecnologias` | Array de tecnologías usadas |
| `status` | `Completado` / `En Progreso` |
| `ilustracion` | Ruta a la ilustración referencial (`public/proyectos/*.svg`) |
| `mockup` | Ruta a la maqueta HTML/CSS/Bootstrap (`public/proyectos/mockups/*.html`) |

Para agregar o editar un proyecto, modifica ese archivo y, si aplica, crea su maqueta en `public/proyectos/mockups/`.

## 🌐 Contacto

* **Email:** cordova23piero@gmail.com
* **LinkedIn:** [Piero Cordova](https://www.linkedin.com/in/piero-cordova-cerna-5a9886318/)
* **GitHub:** [pjcordova](https://github.com/pjcordova)
