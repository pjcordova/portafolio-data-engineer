import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import plotly.graph_objects as go

# --- CONFIGURACIÓN GENERAL (PROFESIONAL) ---
st.set_page_config(
    page_title="Piero Cordova | Data Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS PRO (DISEÑO) ---
st.markdown("""
    <style>
    /* Estilos generales */
    .main { background-color: #0e1117; color: #ffffff; }
    h1 { color: #4facfe; }
    h2 { color: #b0bec5; }
    
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
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 12px;
        margin-right: 5px;
        border: 1px solid #80cbc4;
    }
    
    /* Timeline */
    .timeline-item {
        border-left: 2px solid #4facfe;
        padding-left: 20px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (NAVEGACIÓN) ---
with st.sidebar:
    # Intenta cargar la foto, si no existe no falla
    try:
        st.image("assets/perfil.png", width=120)
    except:
        st.warning("⚠️ Falta 'perfil.png' en assets")

    st.title("Piero Cordova | Data Engineer")
    st.write("🚀 Data Engineer & Systems Student")
    st.markdown("---")

    # Menú de navegación
    menu = st.radio(
        "Navegación:",
        ["🏠 Inicio / Sobre Mí",
         "🏭 Proy 1: ERP Data Warehouse",
         "📈 Proy 2: Peru Market Predictor",
         "🛒 Proy 3: Retail Inventory",
         "📬 Contáctame"]
    )

    st.markdown("---")
    st.caption("© 2026 Piero Cordova Dev")

# ==========================================
# 🏠 PÁGINA: INICIO (SOBRE MÍ)
# ==========================================
if menu == "🏠 Inicio / Sobre Mí":
    # Sección Hero
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("assets/perfil.png",
                     caption="Ingeniero de Sistemas en formación")
        except:
            st.info("📷 (Sube tu foto a assets/perfil.png)")

    with col2:
        st.title("Hola, soy Piero. 👋")
        st.subheader("Transformo datos complejos en soluciones de negocio.")
        st.write("""
        Soy estudiante de Ingeniería de Sistemas con un enfoque práctico en **Ingeniería de Datos** y **Desarrollo Backend**. 
        No solo escribo código; construyo arquitecturas que ayudan a las empresas a tomar mejores decisiones.
        
        Actualmente buscando oportunidades como **Data Analyst** o **Junior Data Engineer**.
        """)

        # Botón de descarga de CV
        try:
            with open("cv_piero.pdf", "rb") as file:
                st.download_button(
                    label="📄 Descargar mi CV",
                    data=file,
                    file_name="CV_Piero_Cordova.pdf",
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.warning(
                "⚠️ Nota: Sube tu archivo 'cv_piero.pdf' a la carpeta del proyecto.")

    st.markdown("---")

    # Sección de Habilidades
    st.subheader("🛠️ Tech Stack & Herramientas")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Lenguaje", "Python 🐍", "Avanzado")
    c2.metric("Database", "MySQL / SQL", "Diseño")
    c3.metric("Frontend", "Streamlit / React", "Intermedio")
    c4.metric("Tools", "Git / Docker", "DevOps")

    # Sección Timeline
    st.markdown("---")
    st.subheader("📅 Mi Trayectoria")
    st.markdown("""
    <div class="timeline-item">
        <strong>2026 - Actualidad</strong><br>
        Desarrollando portafolio Full Stack de Ingeniería de Datos (ERP, Market Prediction).
    </div>
    <div class="timeline-item">
        <strong>2025</strong><br>
        Consultoría de Redes para operaciones de Trading (MikroTik).<br>
        Proyectos académicos de Análisis de Procesos (Nestlé Perú).
    </div>
    <div class="timeline-item">
        <strong>2021 - Presente</strong><br>
        Estudiante de Ingeniería de Sistemas (UTP).
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 🏭 PROYECTO 1: ERP DATA WAREHOUSE
# ==========================================
elif menu == "🏭 Proy 1: ERP Data Warehouse":
    st.title("🚀 Enterprise ERP: Data Warehouse")
    st.markdown("""
    <span class="tech-badge">Python</span> <span class="tech-badge">MySQL</span> <span class="tech-badge">ETL Pipeline</span> <span class="tech-badge">Streamlit</span>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("📖 Ver Descripción y Arquitectura", expanded=True):
        col_desc, col_diag = st.columns([1, 1])
        with col_desc:
            st.write("""
            **El Reto:** Simular la infraestructura de datos de una empresa retail mediana con problemas de dispersión de información.
            
            **La Solución:** * Se diseñó un esquema **Snowflake** en MySQL.
            * Pipeline ETL en Python con **+25,000 transacciones**.
            * Dashboard interactivo para gerencia.
            """)
        with col_diag:
            try:
                st.image("assets/diagrama_er.png",
                         caption="Diagrama E-R (Snowflake)", use_container_width=True)
            except:
                st.info("📷 Falta imagen 'diagrama_er.png' en assets")

    # DEMO EN VIVO
    st.markdown("### 📊 Demo Interactiva")
    try:
        engine = create_engine(
            'mysql+pymysql://root:@localhost/empresa_mediana_db')

        # Filtros
        col_filtro, col_vacio = st.columns([1, 2])
        with col_filtro:
            sucursales = pd.read_sql("SELECT nombre FROM sucursales", engine)
            opcion = st.selectbox("Filtrar por Sede:", [
                                  "Todas"] + list(sucursales['nombre']))

        # Query
        query = """
        SELECT o.fecha, s.nombre as sucursal, c.nombre as categoria, (d.cantidad * d.precio_venta) as total
        FROM ordenes o
        JOIN detalles_orden d ON o.orden_id = d.orden_id
        JOIN sucursales s ON o.sucursal_id = s.sucursal_id
        JOIN productos p ON d.producto_id = p.producto_id
        JOIN categorias c ON p.categoria_id = c.categoria_id
        """
        df = pd.read_sql(query, engine)

        if opcion != "Todas":
            df = df[df['sucursal'] == opcion]

        # Métricas
        m1, m2, m3 = st.columns(3)
        m1.metric("Ingresos Totales", f"${df['total'].sum():,.0f}", "+12%")
        m2.metric("Transacciones", len(df), "+250 hoy")
        m3.metric("Ticket Promedio", f"${df['total'].mean():,.2f}")

        # Gráfico
        trend = df.groupby('fecha')['total'].sum().reset_index()
        fig = px.area(trend, x='fecha', y='total', title="Tendencia de Ingresos",
                      template="plotly_dark", color_discrete_sequence=['#00CC96'])
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error("⚠️ Base de datos ERP no detectada. Asegúrate de encender XAMPP.")

# ==========================================
# 📈 PROYECTO 2: PERU MARKET PREDICTOR
# ==========================================
elif menu == "📈 Proy 2: Peru Market Predictor":
    st.title("📈 Peru Market Predictor")
    st.markdown("""
    <span class="tech-badge">Machine Learning</span> <span class="tech-badge">Scikit-Learn</span> <span class="tech-badge">Python</span> <span class="tech-badge">Finance</span>
    """, unsafe_allow_html=True)

    col_img, col_txt = st.columns([1, 1])

    with col_txt:
        st.markdown("""
        ### Descripción
        Sistema de predicción financiera diseñado para el mercado peruano. Analiza tendencias históricas del **Dólar y Minería** para proyectar comportamientos futuros.
        
        ### Logros Clave
        * Implementación de algoritmos de **Regresión Lineal**.
        * Limpieza de datos financieros reales.
        * Visualización de márgenes de error y confianza.
        """)
        st.link_button("Ver Código en GitHub",
                       "https://github.com/pjcordova/peru-market-predictor")

    with col_img:
        try:
            st.image("assets/market_preview.png",
                     caption="Análisis de Tendencia de Mercado", use_container_width=True)
        except:
            # Fallback
            fechas = pd.date_range(start='2024-01-01', periods=30)
            valores = [3.7 + (x * 0.01) for x in range(30)]
            df_dummy = pd.DataFrame(
                {'Fecha': fechas, 'Tipo de Cambio (Predicción)': valores})
            fig_pred = px.line(
                df_dummy, x='Fecha', y='Tipo de Cambio (Predicción)', markers=True, template="plotly_dark")
            st.plotly_chart(fig_pred, use_container_width=True)

# ==========================================
# 🛒 PROYECTO 3: RETAIL INVENTORY
# ==========================================
elif menu == "🛒 Proy 3: Retail Inventory":
    st.title("🛒 Retail Inventory Analytics")
    st.markdown("""
    <span class="tech-badge">Power BI</span> <span class="tech-badge">SQL</span> <span class="tech-badge">Data Analysis</span>
    """, unsafe_allow_html=True)

    st.info(
        "💡 Este proyecto se enfoca en la visualización estratégica y control de stock.")

    st.markdown("""
    ### El Problema
    El cliente necesitaba reducir las pérdidas por "Stock Muerto" (productos que no se venden) y optimizar la reposición.
    
    ### Mi Solución
    Desarrollé un pipeline que conecta MySQL con Power BI para responder:
    1. **¿Qué productos tienen baja rotación?**
    2. **¿Cuándo debo reabastecer el inventario?**
    """)

    st.link_button("Ver Repositorio en GitHub",
                   "https://github.com/pjcordova/retail-inventory-analytics")

    st.markdown("### 📸 Vista Previa del Dashboard")
    try:
        st.image("assets/dashboard_pbi.png",
                 caption="Tablero de Control de Inventario en Power BI", use_container_width=True)
    except:
        st.warning(
            "⚠️ Sube una captura llamada 'dashboard_pbi.png' a la carpeta assets")

# ==========================================
# 📬 CONTACTO
# ==========================================
elif menu == "📬 Contáctame":
    st.title("¿Listo para trabajar juntos? 🤝")

    col_izq, col_der = st.columns(2)

    with col_izq:
        st.markdown("""
        Actualmente estoy abierto a oportunidades laborales o proyectos freelance.
        
        **¿Por qué contactarme?**
        * ✅ Capacidad probada para construir sistemas desde cero.
        * ✅ Mentalidad orientada a resultados de negocio.
        * ✅ Aprendizaje continuo y rápida adaptación.
        """)

    with col_der:
        st.success("📧 Escríbeme a: piero.cordova@ejemplo.com")
        st.info("📱 WhatsApp: +51 967601604")

# ==========================================
# 👣 FOOTER Y REDES (Se muestra en todas las páginas)
# ==========================================
st.markdown("---")

# 1. Botones de Redes Sociales
st.subheader("🌐 Conectemos")
c_linkedin, c_github, c_email = st.columns(3)

with c_linkedin:
    st.link_button(
        "👔 LinkedIn", "https://www.linkedin.com/in/piero-cordova-cerna-5a9886318", use_container_width=True)

with c_github:
    st.link_button("🐙 GitHub", "https://github.com/pjcordova",
                   use_container_width=True)

with c_email:
    st.link_button(
        "📧 Enviar Email", "mailto:piero.cordova@ejemplo.com", use_container_width=True)

# 2. Copyright
st.markdown("---")
col_footer_izq, col_footer_der = st.columns(2)

with col_footer_izq:
    st.caption("© 2026 Piero Cordova. Todos los derechos reservados.")

with col_footer_der:
    st.caption("Hecho con ❤️ usando Python, Streamlit & Pandas 🐼")
