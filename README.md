# 🚀 Portafolio de Ingeniería de Datos (Full Stack)

![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/Backend-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Supabase](https://img.shields.io/badge/Database-Supabase-3ECF8E?style=for-the-badge&logo=supabase)
![Status](https://img.shields.io/badge/Status-Desplegado-success?style=for-the-badge)

> **Link al Demo en Vivo:** [https://pjcordova-portafolio.streamlit.app](https://pjcordova-portafolio.streamlit.app)

## 📋 Descripción
Este proyecto es una demostración práctica de un ciclo de vida completo del dato (**End-to-End Data Engineering**). 

No es solo una página web estática; es un sistema centralizado que:
1.  **Conecta** a una base de datos en la nube (**PostgreSQL** en Supabase) en tiempo real.
2.  **Procesa** datos crudos utilizando Python y Pandas.
3.  **Visualiza** insights de negocio mediante dashboards interactivos.

El objetivo es demostrar la capacidad de construir infraestructuras de datos escalables, seguras y orientadas a la toma de decisiones.

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Uso en el Proyecto |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Interfaz de usuario interactiva. |
| **Backend** | Python 3.10+ | Lógica de negocio y conexión a BD. |
| **Base de Datos** | Supabase (PostgreSQL) | Almacenamiento persistente en la nube. |
| **Visualización** | Plotly & Power BI | Gráficos dinámicos y dashboards embebidos. |
| **Deploy** | Streamlit Cloud | CI/CD y despliegue automatizado desde GitHub. |

---

## 🏗️ Arquitectura del Sistema

```mermaid
graph LR
A[Usuario] -- HTTPS --> B(Streamlit App)
B -- Query SQL --> C[(Supabase DB)]
C -- Datos --> B
B -- Procesamiento Pandas --> D[Dashboard Interactivo]