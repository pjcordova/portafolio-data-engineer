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
# Esto evita repetir código de conexión a cada rato


def run_query(query_sql):
    try:
        conn = st.connection("supabase", type="sql")
        return conn.query(query_sql, ttl="10m")
    except Exception as e:
        st.error(f"Error de conexión: {e}")
        return pd.DataFrame()


# --- ESTILOS CSS PERSONALIZADOS (MODO PRO) ---
st.markdown("""
    <style>
    /* Fondo y textos generales */
    .main { background-color: #0e1117; color: #ffffff; }
    h1 { color: #4facfe; }
    h2, h3 { color: #b0bec5; }
    
    /* Tarjetas de Proyectos */
    .project-card {
        background-color: #1e2530;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #4facfe;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    /* Badges de Tecnologías */
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
    # Foto de perfil
    try:
        # Intenta cargar la foto nueva si existe, sino la vieja
        st.image("assets/foto_cv.png", width=150)
    except:
        st.warning("📷 Sube tu foto a 'assets/foto_cv.png'")

    st.title("Piero Cordova")
    st.write("🚀 Data Engineer & Full Stack Dev")
    st.markdown("---")

    # MENÚ DE NAVEGACIÓN (Corrección del error 'selected')
    selected = option_menu(
        menu_title="Navegación",
        options=["Inicio", "Proy 1: ERP Data Warehouse",
                 "Proy 2: Peru Market Predictor", "Contacto"],
        icons=["house", "database", "graph-up-arrow", "envelope"],
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
    st.caption("v2.0 - Connected to Supabase Cloud")

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

        # Botón de Descarga de CV
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

    # Sección de Tecnologías
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

    # 1. Ejecutar Query
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
        # KPIs
        total_ingresos = df_erp['total_venta'].sum()
        total_ops = len(df_erp)

        k1, k2 = st.columns(2)
        k1.metric("💰 Ingresos Totales", f"S/ {total_ingresos:,.2f}")
        k2.metric("📦 Operaciones", total_ops)

        # Gráfico
        fig = px.bar(df_erp, x='sucursal', y='total_venta', color='producto',
                     title="Ventas por Sucursal y Producto", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

        with st.expander("Ver Datos Detallados"):
            st.dataframe(df_erp)
    else:
        st.warning("No hay datos en las tablas del ERP (Supabase).")

# ==========================================
# 📈 PROYECTO 2: PERU MARKET PREDICTOR (YA CONECTADO)
# ==========================================
elif selected == "Proy 2: Peru Market Predictor":
    st.title("📈 Tendencias del Mercado Peruano")
    st.markdown("""
    <span class="tech-badge">Time Series</span> <span class="tech-badge">PostgreSQL</span> <span class="tech-badge">Plotly</span>
    """, unsafe_allow_html=True)

    st.write(
        "Visualización de indicadores económicos reales almacenados en la tabla `mercado_peru`.")

    # 1. Traer datos reales de la BD
    query_market = "SELECT fecha, categoria, valor FROM mercado_peru ORDER BY fecha;"
    df_market = run_query(query_market)

    if df_market.empty:
        st.warning(
            "⚠️ La consulta no devolvió datos. Asegúrate de haber corrido el script SQL INSERT en Supabase.")
    else:
        # 2. Asegurar formato de fecha
        df_market['fecha'] = pd.to_datetime(df_market['fecha'])

        # 3. Métricas
        val_max = df_market['valor'].max()
        val_prom = df_market['valor'].mean()

        col1, col2 = st.columns(2)
        col1.metric("Valor Máximo Registrado", f"S/ {val_max:,.2f}")
        col2.metric("Promedio del Periodo", f"S/ {val_prom:,.2f}")

        # 4. Gráfico Interactivo
        tab1, tab2 = st.tabs(["📊 Gráfico de Líneas", "📋 Tabla de Datos"])

        with tab1:
            fig_market = px.line(
                df_market,
                x='fecha',
                y='valor',
                color='categoria',
                markers=True,
                title="Evolución de Categorías en el Tiempo",
                template="plotly_dark"
            )
            st.plotly_chart(fig_market, use_container_width=True)

        with tab2:
            st.dataframe(df_market, use_container_width=True)

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
