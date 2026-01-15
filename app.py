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
        display: inline-block;
        margin-top: 5px;
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
    # Intenta cargar la foto
    try:
        st.image("assets/perfil.png", width=120)
    except:
        st.warning("📷 Falta 'perfil.png' en assets")

    st.title("Piero Cordova")
    st.write("🚀 Data Engineer & Data Science")
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
# 🏠 PÁGINA: INICIO (CONECTADA A SUPABASE)
# ==========================================
if menu == "🏠 Inicio / Sobre Mí":
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("assets/perfil.png",
                     caption="Ingeniero de Sistemas e Informática")
        except:
            st.info("📷 (Sube tu foto a assets/perfil.png)")

    with col2:
        st.title("Bienvenidos Soy Piero Cordova. 👋")
        st.subheader("Ingeniería de Datos con visión estratégica y pasión por crear.")
        st.write("""
        Estudiante de Ingeniería de Sistemas con una curiosidad por el mundo de los datos. Me defino con una mentalidad **Full Stack Data**, disfruto tanto diseñar la arquitectura técnica (Data Engineering) como descubrir las historias ocultas en los datos para la toma de decisiones (Data Science).

        

        Para mí, programar es más que escribir código; es **construir puentes**. Mi objetivo es usar la tecnología para simplificar lo complejo y crear soluciones que realmente ayuden a las personas a tomar mejores decisiones.

        

        🚀 **¿Qué encontrarás aquí?**

        Este portafolio es mi laboratorio de aprendizaje en tiempo real. Aquí combino teoría y práctica, desplegando sistemas en la nube que demuestran no solo lo que sé hacer hoy, sino mi potencial y compromiso para resolver los retos de mañana.
        """)

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

    # --- SECCIÓN PROYECTOS (Desde Supabase) ---
    st.subheader("🚀 Mis Proyectos (Cargados en vivo desde Supabase)")
    st.markdown(
        "Esta sección obtiene los datos directamente de una base de datos **PostgreSQL** en la nube.")

    try:
        conn = st.connection("supabase", type="sql")
        df_proyectos = conn.query(
            "SELECT * FROM proyectos ORDER BY id ASC;", ttl="10m")

        if df_proyectos.empty:
            st.info("La base de datos está conectada pero no tiene proyectos aún.")
        else:
            for index, row in df_proyectos.iterrows():
                with st.container():
                    tech_html = ""
                    if row['tecnologias']:
                        for tech in row['tecnologias']:
                            tech_html += f'<span class="tech-badge">{tech}</span>'

                    st.markdown(f"""
                    <div class="project-card">
                        <h3>{row['nombre']}</h3>
                        <p>{row['descripcion']}</p>
                        <div style="margin-top: 10px;">
                            {tech_html}
                        </div>
                        <br>
                        <a href="{row['url_repo']}" target="_blank" style="text-decoration: none; color: #4facfe; font-weight: bold;">
                            🔗 Ver Código en GitHub
                        </a>
                    </div>
                    """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"⚠️ Error conectando a Supabase: {e}")

    # Skills estáticos
    st.markdown("---")
    st.subheader("🛠️ Tech Stack Global")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Lenguaje", "Python 🐍", "Avanzado")
    c2.metric("Database", "PostgreSQL / SQL", "Cloud")
    c3.metric("Frontend", "Streamlit", "Intermedio")
    c4.metric("DevOps", "Git / Docker", "Básico")


# ==========================================
# 🏭 PROYECTO 1: ERP DATA WAREHOUSE (VIVO 🟢)
# ==========================================
elif menu == "🏭 Proy 1: ERP Data Warehouse":
    st.title("🚀 Enterprise ERP: Data Warehouse")
    st.markdown("""
    <span class="tech-badge">Python</span> <span class="tech-badge">Supabase SQL</span> <span class="tech-badge">ETL Pipeline</span>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 1. Descripción
    with st.expander("📖 Ver Arquitectura Técnica", expanded=False):
        st.write("""
        **Arquitectura Snowflake:** Los datos están normalizados en la nube (Supabase PostgreSQL).
        Se realizan JOINs complejos en tiempo real entre tablas de Dimensiones (Productos, Sucursales) y Tablas de Hechos (Ordenes).
        """)

    # 2. CONEXIÓN A LA NUBE Y DASHBOARD
    try:
        conn = st.connection("supabase", type="sql")

        # A. Consultamos las sucursales para el filtro
        df_sucursales = conn.query("SELECT nombre FROM sucursales;", ttl="10m")

        if df_sucursales.empty:
            st.warning(
                "⚠️ No se encontraron sucursales. Corre el script SQL de carga de datos.")
        else:
            lista_sucursales = ["Todas"] + df_sucursales['nombre'].tolist()

            # Filtros en la interfaz
            col_filtro, _ = st.columns([1, 2])
            with col_filtro:
                opcion_sucursal = st.selectbox(
                    "📍 Filtrar por Sede:", lista_sucursales)

            # B. QUERY COMPLEX (JOINs)
            query = """
            SELECT 
                o.fecha,
                s.nombre as sucursal,
                c.nombre as categoria,
                p.nombre as producto,
                (d.cantidad * d.precio_venta) as total_venta
            FROM ordenes o
            JOIN detalles_orden d ON o.orden_id = d.orden_id
            JOIN sucursales s ON o.sucursal_id = s.sucursal_id
            JOIN productos p ON d.producto_id = p.producto_id
            JOIN categorias c ON p.categoria_id = c.categoria_id
            ORDER BY o.fecha ASC;
            """

            # Ejecutamos la query
            df_ventas = conn.query(query, ttl="10m")

            if df_ventas.empty:
                st.info("No hay ventas registradas todavía.")
            else:
                # C. Aplicamos filtro de Python
                if opcion_sucursal != "Todas":
                    df_ventas = df_ventas[df_ventas['sucursal']
                                          == opcion_sucursal]

                # D. CÁLCULO DE KPIS
                total_ingresos = df_ventas['total_venta'].sum()
                total_transacciones = len(df_ventas)
                ticket_promedio = df_ventas['total_venta'].mean(
                ) if total_transacciones > 0 else 0

                st.markdown("### 📊 Tablero de Control en Tiempo Real")

                # Métricas visuales
                m1, m2, m3 = st.columns(3)
                m1.metric("💰 Ingresos Totales", f"S/ {total_ingresos:,.2f}")
                m2.metric("📦 Transacciones", f"{total_transacciones}")
                m3.metric("🎫 Ticket Promedio", f"S/ {ticket_promedio:,.2f}")

                # E. GRÁFICOS AVANZADOS (PLOTLY)
                c_chart1, c_chart2 = st.columns(2)

                with c_chart1:
                    st.caption("Tendencia de Ingresos por Fecha")
                    trend_df = df_ventas.groupby(
                        'fecha')['total_venta'].sum().reset_index()
                    fig_trend = px.area(trend_df, x='fecha', y='total_venta',
                                        template="plotly_dark", color_discrete_sequence=['#4facfe'])
                    st.plotly_chart(fig_trend, use_container_width=True)

                with c_chart2:
                    st.caption("Distribución por Categoría")
                    fig_pie = px.pie(df_ventas, values='total_venta', names='categoria',
                                     template="plotly_dark", hole=0.4)
                    st.plotly_chart(fig_pie, use_container_width=True)

                with st.expander("🔎 Ver Datos Crudos"):
                    st.dataframe(df_ventas)

    except Exception as e:
        st.error(f"Error conectando al Data Warehouse: {e}")
        st.info("💡 Asegúrate de haber corrido el Script SQL de tablas en Supabase.")

# ==========================================
# 📈 PROYECTO 2: PERU MARKET PREDICTOR
# ==========================================
elif selected == "Proy 2: Peru Market Predictor":
    st.title("📈 Tendencias del Mercado Peruano")
    st.markdown("""
    Esta sección visualiza datos reales almacenados en la nube (**Supabase**).
    Demuestra la capacidad de realizar consultas SQL (`SELECT`) y renderizar series de tiempo.
    """)

    # 1. Traer datos reales de la BD
    try:
        query_market = "SELECT fecha, categoria, valor FROM mercado_peru ORDER BY fecha;"
        df_market = run_query(query_market)

        if df_market.empty:
            st.warning(
                "⚠️ La consulta no devolvió datos. Revisa si insertaste las filas en Supabase.")
        else:
            # 2. Asegurar formato de fecha
            df_market['fecha'] = pd.to_datetime(df_market['fecha'])

            # 3. Métricas calculadas en Python
            total_valor = df_market['valor'].sum()
            promedio_valor = df_market['valor'].mean()

            col1, col2, col3 = st.columns(3)
            col1.metric("Registros Totales", len(df_market))
            col2.metric("Valor Total Mercado", f"S/ {total_valor:,.2f}")
            col3.metric("Ticket Promedio", f"S/ {promedio_valor:,.2f}")

            # 4. Gráfico Interactivo
            tab1, tab2 = st.tabs(["📊 Gráfico de Líneas", "📋 Datos Crudos"])

            with tab1:
                fig_market = px.line(
                    df_market,
                    x='fecha',
                    y='valor',
                    color='categoria',
                    markers=True,
                    title="Evolución de Ventas por Categoría",
                    labels={'valor': 'Monto (PEN)',
                            'fecha': 'Fecha de Registro'}
                )
                st.plotly_chart(fig_market, use_container_width=True)

            with tab2:
                st.dataframe(df_market, use_container_width=True)

    except Exception as e:
        st.error(f"Error al conectar con la base de datos: {e}")

# ==========================================
# 🛒 PROYECTO 3: RETAIL INVENTORY
# ==========================================
elif menu == "🛒 Proy 3: Retail Inventory":
    st.title("🛒 Retail Inventory Analytics")
    st.markdown('<span class="tech-badge">Power BI</span> <span class="tech-badge">SQL</span>',
                unsafe_allow_html=True)
    st.write(
        "Visualización estratégica para control de stock y reducción de pérdidas.")

    try:
        st.image("assets/dashboard_pbi.png",
                 caption="Dashboard Power BI", use_container_width=True)
    except:
        st.warning("⚠️ Sube una captura llamada 'dashboard_pbi.png'")

# ==========================================
# 📬 CONTACTO
# ==========================================
elif menu == "📬 Contáctame":
    st.title("¿Listo para trabajar juntos? 🤝")
    col_izq, col_der = st.columns(2)
    with col_izq:
        st.markdown("""
        **¿Por qué contactarme?**
        * ✅ Capacidad probada para construir sistemas Full Stack.
        * ✅ Dominio de Cloud Databases (Supabase/AWS).
        """)
    with col_der:
        st.success("📧 Escríbeme a: cordova23piero@gmail.com")
        st.info("📱 LinkedIn: Ver perfil")

# ==========================================
# 👣 FOOTER
# ==========================================
st.markdown("---")
c_lk, c_gh, c_mail = st.columns(3)
with c_lk:
    st.link_button(
        "👔 LinkedIn", "https://www.linkedin.com/in/piero-cordova-cerna-5a9886318", use_container_width=True)
with c_gh:
    st.link_button("🐙 GitHub", "https://github.com/pjcordova",
                   use_container_width=True)
with c_mail:
    st.link_button("📧 Email", "mailto:cordova23piero@gmail.com",
                   use_container_width=True)

st.markdown("---")
st.caption("© 2026 Piero Cordova | Hecho con Python, Streamlit & Supabase ⚡")
