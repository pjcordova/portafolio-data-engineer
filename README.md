# Cordova Solutions

![Vue](https://img.shields.io/badge/Frontend-Vue%203-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white)
![TypeScript](https://img.shields.io/badge/Lang-TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Vite](https://img.shields.io/badge/Build-Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Styles-TailwindCSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![Supabase](https://img.shields.io/badge/Database-Supabase-3ECF8E?style=for-the-badge&logo=supabase)
![Vercel](https://img.shields.io/badge/Hosting-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

## 📋 Descripción

Sitio corporativo de **Cordova Solutions**, desarrollado en Vue 3 + Tailwind CSS, que presenta casos de éxito reales en desarrollo Full Stack, ERPs, e-commerce y soluciones cloud.

Los proyectos mostrados en la sección "Casos de Éxito" **no están hardcodeados**: se consultan en tiempo real desde una tabla `proyectos` en Supabase (PostgreSQL), lo que permite actualizar el portafolio sin volver a desplegar el sitio.

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Uso en el Proyecto |
| :--- | :--- | :--- |
| **Frontend** | Vue 3 + Vite + TypeScript | SPA con composición reactiva y tipado estático. |
| **Estilos** | Tailwind CSS | Sistema de diseño utilitario, responsive. |
| **Base de Datos** | Supabase (PostgreSQL) | Fuente de verdad de los proyectos mostrados. |
| **Cliente DB** | `@supabase/supabase-js` | Consulta de la tabla `proyectos` vía API REST/anon key. |
| **Hosting** | Vercel | Build estático (`vite build`) con despliegue continuo. |

## 🚀 Desarrollo Local

```bash
npm install
cp .env.example .env   # completa VITE_SUPABASE_URL y VITE_SUPABASE_ANON_KEY
npm run dev
```

Build de producción:

```bash
npm run build
npm run preview
```

## 🗄️ Estructura de datos (`proyectos`)

Cada fila representa un caso de éxito mostrado en el sitio:

| Columna | Descripción |
| :--- | :--- |
| `nombre` | Nombre del proyecto |
| `cliente` | Cliente o "Uso interno" |
| `categoria_solucion` | Categoría (E-commerce, ERP, EdTech, etc.) |
| `problema_resuelto` | Descripción del problema que resuelve |
| `metrica_impacto` | Resultado/impacto medible (opcional) |
| `tecnologias` | Array de tecnologías usadas |
| `status` | `Completado` / `En Progreso` |
| `link_demo` | URL del demo en vivo (opcional) |
| `link_figma` | URL del diseño en Figma (opcional) |

## 🌐 Contacto

* **Email:** cordova23piero@gmail.com
* **LinkedIn:** [Piero Cordova](https://www.linkedin.com/in/piero-cordova-cerna-5a9886318/)
* **GitHub:** [pjcordova](https://github.com/pjcordova)
