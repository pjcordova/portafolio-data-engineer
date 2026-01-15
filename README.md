# 🚀 Portafolio de Ingeniería de Datos & ML (Full Stack)

![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/Backend-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Supabase](https://img.shields.io/badge/Database-Supabase-3ECF8E?style=for-the-badge&logo=supabase)
![Scikit-Learn](https://img.shields.io/badge/AI-Scikit%20Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

> **Link al Demo en Vivo:** [https://pjcordova-portafolio.streamlit.app](https://pjcordova-portafolio.streamlit.app)

## 📋 Descripción
Este proyecto es una demostración práctica de una arquitectura de datos moderna (**End-to-End Data Engineering**). 

Va más allá de un dashboard tradicional: es un sistema inteligente que conecta bases de datos en la nube, procesa información en tiempo real y utiliza algoritmos de **Machine Learning** para proyectar tendencias futuras.

### 💡 Características Clave:
1.  **Data Warehouse Cloud:** Conexión en tiempo real a **Supabase (PostgreSQL)**.
2.  **ETL Pipeline:** Extracción y transformación de datos con Pandas.
3.  **Machine Learning:** Módulo de predicción basado en **Regresión Lineal** (Scikit-Learn) para forecasting de ventas a 30 días.
4.  **Interactive Dashboard:** Visualización avanzada con Plotly y Streamlit.

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Uso en el Proyecto |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | UI Interactiva y navegación. |
| **Backend** | Python 3.10+ | Lógica de negocio y orquestación. |
| **Database** | Supabase (PostgreSQL) | Almacenamiento persistente y relacional. |
| **AI / ML** | Scikit-Learn | Entrenamiento de modelo de Regresión Lineal. |
| **Viz** | Plotly Express | Gráficos interactivos y series de tiempo. |

---

## 🏗️ Arquitectura del Sistema

```mermaid
graph LR
A[Usuario] -- HTTPS --> B(Streamlit App)
B -- SQL Query --> C[(Supabase DB)]
C -- Datos Históricos --> B
B -- Pandas --> D{Motor ML (Scikit-Learn)}
D -- Entrenamiento --> E[Modelo Regresión Lineal]
E -- Predicción (30 días) --> F[Gráfico Forecast]
F --> A