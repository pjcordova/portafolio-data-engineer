# 🚀 Portafolio de Ingeniería de Datos & ML (Full Stack)

![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/Backend-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Supabase](https://img.shields.io/badge/Database-Supabase-3ECF8E?style=for-the-badge&logo=supabase)
![Scikit-Learn](https://img.shields.io/badge/AI-Scikit%20Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

> **Link al Demo en Vivo:** [https://pjcordova-portafolio.streamlit.app](https://pjcordova-portafolio.streamlit.app)

## 📋 Descripción
Este proyecto es una demostración práctica de una arquitectura de datos moderna (**End-to-End Data Engineering**).

Va más allá de un dashboard tradicional: es un sistema inteligente que centraliza operaciones de datos. Conecta bases de datos en la nube para análisis histórico y despliega modelos de **Machine Learning (IA)** para anticipar eventos futuros, como tendencias de ventas y comportamiento de clientes.

### 💡 Características Clave:
1.  **Data Warehouse Cloud:** Conexión en tiempo real a **Supabase (PostgreSQL)**.
2.  **ETL Pipeline:** Extracción, limpieza y transformación de datos con Pandas.
3.  **Sales Forecasting:** Predicción de ventas futuras mediante **Regresión Lineal**.
4.  **Churn Prediction (Nuevo):** Sistema de clasificación con **Random Forest** para detectar clientes en riesgo de fuga.
5.  **Interactive Dashboard:** Visualización avanzada con Plotly y Streamlit.

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Uso en el Proyecto |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | UI Interactiva, navegación y formularios dinámicos. |
| **Backend** | Python 3.10+ | Lógica de negocio, orquestación y carga de modelos. |
| **Database** | Supabase (PostgreSQL) | Almacenamiento persistente y relacional. |
| **AI / ML** | Scikit-Learn | Entrenamiento de modelos (Regresión y Clasificación). |
| **Persistencia** | Joblib | Serialización de modelos entrenados (.pkl). |
| **Viz** | Plotly Express | Gráficos interactivos y series de tiempo. |

---

## 🧩 Módulos del Portafolio

### 🔹 Proyecto 1-3: Análisis de Retail & Inventario
Sistema conectado a Base de Datos para gestión de inventarios y predicción de mercado peruano.
* **Tech:** SQL, Pandas, Plotly.
* **Impacto:** Optimización de stock basada en datos históricos.

### 🔹 Proyecto 4: Predicción de Fuga de Clientes (Churn) 🧠
Modelo de Inteligencia Artificial diseñado para retención de clientes en telecomunicaciones.
* **Modelo:** Random Forest Classifier.
* **Métrica:** 77.5% Accuracy.
* **Input:** El usuario ingresa datos (Contrato, Pagos, Antigüedad) en tiempo real.
* **Output:** Probabilidad de abandono (%) y alerta de riesgo.

---

## 🏗️ Arquitectura del Sistema

```mermaid
graph LR
    A["Usuario"] -- Interactúa --> B("Streamlit App")
    
    subgraph "Capa de Datos (Data Layer)"
    B -- SQL Query --> C[("Supabase DB")]
    C -- Datos Históricos --> B
    end
    
    subgraph "Capa de Inteligencia (ML Layer)"
    B -- Input Usuario --> D{"Preprocesamiento"}
    D -- Features --> E["Modelo .pkl (Random Forest)"]
    E -- Inferencia --> B
    end

    B -- Resultados Visuales --> A

📦 Instalación Local
Si deseas correr este proyecto en tu máquina:

Clonar el repositorio:

Bash
git clone [https://github.com/pjcordova/portafolio-data-engineer.git](https://github.com/pjcordova/portafolio-data-engineer.git)
Instalar dependencias:

Bash
pip install -r requirements.txt
Ejecutar la aplicación:

Bash
streamlit run app.py

Desarrollado por Piero Cordova | Data Engineer & ML Enthusiast