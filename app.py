import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go #

# Configuración de la página
st.set_page_config(page_title="Universidad Dashboard", layout="wide", page_icon="🎓") #Titulo de la pestaña y diseño, wide ocupa toda la pantalla

# Cargar datos
df = pd.read_csv('university_student_data.csv')

# Título
st.title("Datos Universitarios - Tendencias y Análisis")

# Sidebar con filtros
st.sidebar.header("Filtros")
anosFiltro = st.sidebar.multiselect(
    "Selecciona año:",
    options=df['Year'].unique(), #Lista de años únicos en la columna 'Year'
    default=df['Year'].unique() ) #Por defecto todos los años están seleccionados

estacionFiltro = st.sidebar.multiselect(
    "Selecciona estación del año:",
    options=df['Term'].unique(), #Lista de estaciones únicas en la columna 'Term'
    default=df['Term'].unique() ) #Por defecto todas las estaciones están seleccionados

# Filtrar datos
datosFiltrado = df[(df['Year'].isin(anosFiltro)) & (df['Term'].isin(estacionFiltro))]


totalAnos = sorted(df['Year'].unique())
seleccionAnos = sorted(anosFiltro)

if not seleccionAnos:
    textoAnosSeleccionados = "No seleccionaste ningún año."
elif set(seleccionAnos) == set(totalAnos):
    textoAnosSeleccionados = f"Estas viendo la información de:  {min(totalAnos)} - {max(totalAnos)}"
else:
    textoAnosSeleccionados = "Estas viendo la información de : " + ", ".join(str(y) for y in seleccionAnos)

st.write(textoAnosSeleccionados)

# KPIs principales, estructura de 4 columnas
st.subheader("KPIs")
col1, col2, col3, col4 = st.columns(4)

with col1: st.metric("Total Aplicaciones", f"{datosFiltrado['Applications'].sum():,}")
with col2: st.metric("Total Admitidos", f"{datosFiltrado['Admitted'].sum():,}")
with col3: st.metric("Total Matriculados", f"{datosFiltrado['Enrolled'].sum():,}")
with col4:
    promedioSatisfaccion = datosFiltrado['Student Satisfaction (%)'].mean()
    st.metric("Satisfacción Promedio", f"{promedioSatisfaccion:.1f}%") #cuando un bloque lleva más de una instrucción, debe seguir esta estructura

# Gráficos
st.subheader("Tendencias")
st.write("Para ver las tendencias a lo largo del tiempo, se presentan los siguientes gráficos:")
col1, col2 = st.columns(2) # Dividir en dos columnas
#El primer grafico es de lineas, la idea es ver la tendencia de aplicaciones, admitidos y matriculados a lo largo del tiempo
with col1:
    st.write("Aquí podemos ver las tendencias de aplicaciones, admitidos y matriculados a lo largo del tiempo.")

    fig1 = go.Figure()  #Reciben para x años y para y aplicaciones, admitidos y matriculados, name es la leyenda, mode es el tipo de grafico
    fig1.add_trace(go.Scatter(x=datosFiltrado['Year'], y=datosFiltrado['Applications'], name='Aplicaciones', mode='lines+markers'))
    fig1.add_trace(go.Scatter(x=datosFiltrado['Year'], y=datosFiltrado['Admitted'], name='Admitidos', mode='lines+markers'))
    fig1.add_trace(go.Scatter(x=datosFiltrado['Year'], y=datosFiltrado['Enrolled'], name='Matriculados', mode='lines+markers'))
    fig1.update_layout(title="Tendencia de admisión", xaxis_title="Año", yaxis_title="Cantidad") # Títulos de los ejes
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.write("Aquí podemos ver las tasas de retención y satisfacción de los estudiantes a lo largo del tiempo.")

    fig2 = go.Figure() #Reciben para x años y para y tasas de retención y satisfacción, name es la leyenda, mode es el tipo de grafico
    fig2.add_trace(go.Scatter(x=datosFiltrado['Year'], y=datosFiltrado['Retention Rate (%)'], name='Retención', mode='lines+markers'))
    fig2.add_trace(go.Scatter(x=datosFiltrado['Year'], y=datosFiltrado['Student Satisfaction (%)'], name='Satisfacción', mode='lines+markers'))
    fig2.update_layout(title="Tasas de retencion y satisfacción", xaxis_title="Año", yaxis_title="Porcentaje")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Distribución por carrera")
st.write("Para entender como se distribuyen los estudiantes entre las diferentes carreras, se presentan los siguientes gráficos:")

# Distribucion de datos por carrera
datosCarrerasFiltro = datosFiltrado[['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']].sum()

col1, col2 = st.columns(2)

with col1:
    # Gráfico de pastel
    fig3 = px.pie(values=datosCarrerasFiltro.values, names=datosCarrerasFiltro.index, title="Distribución de matriculados en cada carrera")
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    # Gráfico de barras apiladas por año
    dfCarreras = datosFiltrado.groupby('Year')[['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']].sum()
    fig4 = go.Figure() #Los años son el indice, y las carreras son las barras apiladas, cantidad de matriculados por carrera y año
    fig4.add_trace(go.Bar(x=dfCarreras.index, y=dfCarreras['Engineering Enrolled'], name='Ingeniería'))
    fig4.add_trace(go.Bar(x=dfCarreras.index, y=dfCarreras['Business Enrolled'], name='Negocios'))
    fig4.add_trace(go.Bar(x=dfCarreras.index, y=dfCarreras['Arts Enrolled'], name='Artes'))
    fig4.add_trace(go.Bar(x=dfCarreras.index, y=dfCarreras['Science Enrolled'], name='Ciencias'))
    fig4.update_layout(barmode='stack', title="Matriculados por carrera y año", xaxis_title="Año")
    st.plotly_chart(fig4, use_container_width=True)


# Tabla de datos,
st.subheader("Datos completos")
st.write("A continuación se muestra la tabla completa de datos filtrados según las selecciones realizadas:")
st.dataframe(datosFiltrado, use_container_width=True)


# Estadísticas descriptivas
st.write("Si deseas ver estadísticas descriptivas de los datos filtrados, puedes activar la siguiente opción:")
if st.checkbox("Mostrar estadísticas descriptivas"):
    st.write(datosFiltrado.describe())