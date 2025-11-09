## Descripción general

Se presenta un panel interactivo desarrollado con Streamlit que permite visualizar la evolución de métricas clave universitarias entre 2015 y 2024.
El dashboard ofrece una visión integral de las solicitudes, admisiones, matrículas, tasas de retención y satisfacción estudiantil.

## Proposito
Aplicación Streamlit para visualizar y analizar datos universitarios: tendencias temporales, KPIs (aplicaciones, admitidos, matriculados, satisfacción), distribución por carrera y estadísticas descriptivas. Permite filtrar por año y estación del año.

## Uso
- Sidebar: Para seleccionar años y estaciones.  
- Vista principal:
  - Encabezado que indica los años que se están visualizando.
  - KPIs principales (aplicaciones, admitidos, matriculados, satisfacción).
  - Gráficos de tendencias (líneas), tasas (líneas), distribución por carrera (pastel) y barras apiladas por año.
  - Tabla de datos filtrados y opción para ver estadísticas descriptivas.


## Estructura del dataset  
El archivo `university_student_data.csv` contiene la siguiente estructura:

| Columna | Descripción |
|----------|--------------|
| **Year** | Año académico |
| **Term** | Periodo académico (Spring/Fall) |
| **Applications** | Total de solicitudes recibidas |
| **Admitted** | Número de estudiantes admitidos |
| **Enrolled** | Número de estudiantes matriculados |
| **Retention Rate (%)** | Porcentaje de retención estudiantil |
| **Student Satisfaction (%)** | Porcentaje de satisfacción estudiantil |
| **Engineering Enrolled** | Estudiantes matriculados en Ingeniería |
| **Business Enrolled** | Estudiantes matriculados en Negocios |
| **Arts Enrolled** | Estudiantes matriculados en Artes |
| **Science Enrolled** | Estudiantes matriculados en Ciencias |


## Autores 
- Cantú Olivarez Arturo - 10919
- Cruz Cervantes Diego Sebastián - 10032
