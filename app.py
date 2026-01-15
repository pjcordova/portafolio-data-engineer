import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from sqlalchemy import text

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Piero Cordova | Data Engineer Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FUNCIÓN HELPER PARA BASE DE DATOS (SUPABASE) ---


def run_query(query_sql):
    try:
        conn = st.connection("supabase", type="sql")
        return conn.query(query_sql, ttl="10m")
    except Exception as e:
        st.error(f"Error de conexión: {e}")
        return pd.DataFrame()


# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    h1 { color: #4facfe; }
    h2, h3 { color: #b0bec5; }
    .project-card {
        background-color: #1e2530;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #4facfe;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .tech-badge {
        background-color: #263238;
        color: #80cbc4;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        border: 1px solid #80cbc4;
        margin-right: 5px;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    try:
        st.image("assets/foto_cv.png", width=150)
    except:
        st.warning("📷 Sube tu foto a 'assets/foto_cv.png'")

    st.title("Piero Cordova")
    st.write("🚀 Data Engineer & Full Stack Dev")
    st.markdown("---")

    # MENÚ DE NAVEGACIÓN COMPLETO
    selected = option_menu(
        menu_title="Navegación",
        options=[
            "Inicio",
            "Proy 1: ERP Data Warehouse",
            "Proy 2: Peru Market Predictor",
            "Proy 3: Retail Inventory",
            "Contacto"
        ],
        icons=["house", "database", "graph-up-arrow", "cart", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0e1117"},
            "icon": {"color": "orange", "font-size": "18px"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#262730"},
            "nav-link-selected": {"background-color": "#4facfe"},
        }
    )

    st.markdown("---")
    st.caption("© 2026 Piero Cordova Portafolio")

# ==========================================
# 🏠 PÁGINA: INICIO
# ==========================================
if selected == "Inicio":
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("assets/foto_cv.png", width=250,
                 caption="Piero Cordova | Ingeniero de Sistemas")

    with col2:
        st.title("¡Hola! Soy Piero Cordova 👋")
        st.subheader(
            "Transformando datos complejos en decisiones estratégicas.")
        st.write("""
        Soy estudiante de **Ingeniería de Sistemas e Informática** (9no ciclo UTP) con experiencia real en integración de sistemas.
        
        Me especializo en el ciclo de vida completo del dato (**End-to-End Data Engineering**):
        desde la extracción en bases de datos transaccionales, pasando por pipelines de transformación en Python, 
        hasta la visualización en dashboards interactivos.
        """)

        try:
            with open("cv_piero.pdf", "rb") as file:
                st.download_button(
                    label="📄 Descargar CV Profesional",
                    data=file,
                    file_name="CV_Piero_Cordova.pdf",
                    mime="application/pdf",
                    type="primary"
                )
        except:
            st.warning(
                "⚠️ Recuerda subir tu archivo 'cv_piero.pdf' a la carpeta del proyecto.")

    st.markdown("---")
    st.subheader("🛠️ Tech Stack & Herramientas")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Lenguaje", "Python 🐍", "Data Science")
    c2.metric("Base de Datos", "PostgreSQL", "Supabase Cloud")
    c3.metric("Framework", "Streamlit", "Full Stack")
    c4.metric("BI Tool", "Power BI", "Dashboards")

# ==========================================
# 🏭 PROYECTO 1: ERP DATA WAREHOUSE
# ==========================================
elif selected == "Proy 1: ERP Data Warehouse":
    st.title("🏭 Enterprise ERP: Data Warehouse")
    st.markdown("""
    <span class="tech-badge">Python</span> <span class="tech-badge">SQL Join</span> <span class="tech-badge">KPIs en Tiempo Real</span>
    """, unsafe_allow_html=True)

    st.info("Este módulo conecta dos tablas de Supabase (`ordenes` y `detalles`) para calcular ventas totales.")

    query_erp = """
    SELECT 
        o.fecha,
        s.nombre as sucursal,
        p.nombre as producto,
        (d.cantidad * d.precio_venta) as total_venta
    FROM ordenes o
    JOIN detalles_orden d ON o.orden_id = d.orden_id
    JOIN sucursales s ON o.sucursal_id = s.sucursal_id
    JOIN productos p ON d.producto_id = p.producto_id
    ORDER BY o.fecha DESC;
    """
    df_erp = run_query(query_erp)

    if not df_erp.empty:
        total_ingresos = df_erp['total_venta'].sum()
        total_ops = len(df_erp)

        k1, k2 = st.columns(2)
        k1.metric("💰 Ingresos Totales", f"S/ {total_ingresos:,.2f}")
        k2.metric("📦 Operaciones", total_ops)

        fig = px.bar(df_erp, x='sucursal', y='total_venta', color='producto',
                     title="Ventas por Sucursal y Producto", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

        with st.expander("Ver Datos Detallados"):
            st.dataframe(df_erp)
    else:
        st.warning("No hay datos en las tablas del ERP (Supabase).")

# ==========================================
# 📈 PROYECTO 2: PERU MARKET PREDICTOR
# ==========================================
# ==========================================
# 📈 PROYECTO 2: PERU MARKET PREDICTOR (CON ML)
# ==========================================
elif selected == "Proy 2: Peru Market Predictor":
    st.title("🤖 Peru Market Predictor (AI Powered)")
    st.markdown("""
    <span class="tech-badge">Machine Learning</span> <span class="tech-badge">Scikit-Learn</span> <span class="tech-badge">Forecasting</span>
    """, unsafe_allow_html=True)

    st.write("""
    Este módulo utiliza un modelo de **Regresión Lineal** para analizar el historial de precios 
    y proyectar la tendencia futura a 30 días.
    """)

    # 1. Traer datos
    query_market = "SELECT fecha, categoria, valor FROM mercado_peru ORDER BY fecha;"
    df_market = run_query(query_market)

    if df_market.empty:
        st.warning("⚠️ No hay datos para predecir.")
    else:
        df_market['fecha'] = pd.to_datetime(df_market['fecha'])

        # 2. Selector de Categoría (Para que la predicción sea lógica)
        lista_cats = df_market['categoria'].unique().tolist()
        cat_seleccionada = st.selectbox(
            "🎯 Selecciona la categoría a predecir:", lista_cats)

        # Filtrar datos por esa categoría
        df_filtered = df_market[df_market['categoria']
                                == cat_seleccionada].copy()

        # --- MOTOR DE MACHINE LEARNING (SCIKIT-LEARN) ---
        from sklearn.linear_model import LinearRegression
        import numpy as np

        # Preparamos los datos para el modelo (Fechas a números)
        df_filtered['fecha_num'] = df_filtered['fecha'].map(
            pd.Timestamp.toordinal)

        X = df_filtered[['fecha_num']]  # Features (Fechas)
        y = df_filtered['valor']       # Target (Valores)

        # Entrenar el modelo
        model = LinearRegression()
        model.fit(X, y)

        # Generar fechas futuras (Próximos 30 días)
        ultima_fecha = df_filtered['fecha'].max()
        fechas_futuras = [ultima_fecha +
                          pd.Timedelta(days=x) for x in range(1, 31)]
        fechas_futuras_num = [
            [pd.Timestamp(f).toordinal()] for f in fechas_futuras]

        # Predecir valores futuros
        predicciones = model.predict(fechas_futuras_num)

        # Crear dataframe de predicción
        df_pred = pd.DataFrame({
            'fecha': fechas_futuras,
            'valor': predicciones,
            'categoria': f"{cat_seleccionada} (Predicción)",
            'tipo': 'Proyección IA'
        })

        # Etiquetar datos históricos
        df_filtered['tipo'] = 'Histórico Real'

        # Unir Histórico + Futuro
        df_final = pd.concat([df_filtered, df_pred])

        # --- VISUALIZACIÓN ---
        st.markdown("### 🔮 Proyección de Tendencia")

        # KPIs de Predicción
        tendencia = "Alza 📈" if predicciones[-1] > y.iloc[-1] else "Baja 📉"
        var_mes = ((predicciones[-1] - y.iloc[-1]) / y.iloc[-1]) * 100

        col1, col2 = st.columns(2)
        col1.metric("Tendencia a 30 días", tendencia)
        col2.metric("Variación Estimada", f"{var_mes:.2f}%")

        # Gráfico con línea punteada para el futuro
        fig_pred = px.line(
            df_final,
            x='fecha',
            y='valor',
            color='tipo',
            line_dash='tipo',  # Punteado para la predicción
            title=f"Histórico vs Predicción: {cat_seleccionada}",
            template="plotly_dark",
            color_discrete_map={
                'Histórico Real': '#00CC96', 'Proyección IA': '#EF553B'}
        )
        st.plotly_chart(fig_pred, use_container_width=True)

        with st.expander("🔎 Ver explicación técnica del modelo"):
            st.write(f"""
            **Ecuación del Modelo:** y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}
            
            El algoritmo ha detectado una pendiente de **{model.coef_[0]:.4f}**. 
            Esto significa que por cada día que pasa, el valor cambia aproximadamente en esa magnitud.
            """)

# ==========================================
# 🛒 PROYECTO 3: RETAIL INVENTORY
# ==========================================
elif selected == "Proy 3: Retail Inventory":
    st.title("🛒 Retail Inventory Analytics")
    st.markdown('<span class="tech-badge">Power BI</span> <span class="tech-badge">SQL</span>',
                unsafe_allow_html=True)
    st.write(
        "Visualización estratégica para control de stock y reducción de pérdidas.")

    try:
        # Asegúrate de tener la imagen 'dashboard_pbi.png' en la carpeta assets
        st.image("assets/dashboard_pbi.png",
                 caption="Dashboard Power BI", use_container_width=True)
    except:
        st.warning(
            "⚠️ Falta la imagen: Sube una captura llamada 'dashboard_pbi.png' a la carpeta assets.")

# ==========================================
# 📬 PÁGINA: CONTACTO
# ==========================================
elif selected == "Contacto":
    st.title("📬 Conectemos")

    c1, c2 = st.columns(2)
    with c1:
        st.image("assets/foto_cv.png", width=200)
    with c2:
        st.success(
            "Estoy disponible para oportunidades como Data Engineer o Analista de Datos.")
        st.markdown("""
        * **Email:** cordova23piero@gmail.com
        * **LinkedIn:** [Ver Perfil](https://www.linkedin.com/in/piero-cordova-6a208316a/)
        * **GitHub:** [Ver Repositorio](https://github.com/pjcordova)
        """)

# --- FOOTER ---
st.markdown("---")
st.caption("Desarrollado por Piero Cordova | 2026")
