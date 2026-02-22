## 🚦 Análisis de Accidentes de Tráfico en Madrid 2024

### 📌 Objetivo

El objetivo principal es identificar patrones espacio-temporales y factores de riesgo (alcohol, perfiles de edad, franjas horarias) que influyen en la gravedad y frecuencia de los accidentes en la capital para apoyar la toma de decisiones en seguridad vial.

Además poder identificar entre otros:

- Distritos con mayor siniestralidad.
- Tipos de accidente más frecuentes bajo influencia de alcohol y porcentaje que representan.
- Influencia de las condiciones meteorológicas.
- Franja horaria recurrente por días con más accidentalidad.


### 2) 📂 Dataset
- Fuente: Archivo CSV (2024_Accidentalidad.csv)
- Fuente oficial: Portal de Datos Abiertos del Ayuntamiento de Madrid  
- 🔗 https://datos.madrid.es/
- Nº filas/columnas: 49340 / 19
- Variables clave: fecha, hora, distrito, tipo_accidente, tipo_vehiculo, tipo_persona, rango_edad, sexo, positiva_alcohol, positiva_droga

### 3) ❓ Preguntas
- Q1: ¿Cómo se distribuyen los datos después de la limpieza?
- Q2: ¿Qué características nuevas se pueden derivar?
- Q3: ¿Qué insights se obtienen de las visualizaciones?
- Q4: ¿Cuáles son los distritos con mayor siniestralidad y qué relación tienen con el consumo de alcohol?
- Q5: ¿En qué franjas horarias y días de la semana se concentra el mayor riesgo de accidentes graves?

### 4) Data issues & fixes
- Valores faltantes → Limpieza y imputación en src/cleaning.py
- Formatos incorrectos → Conversión de tipos de datos
- Fechas y Horas inconsistentes → Conversión a objetos datetime y extracción de componentes (hora, día de la semana, mes).
- Eficiencia de memoria → Conversión de columnas de texto repetitivo a tipo category (reducción de uso de memoria en >50%).

### 5) 🔄 Pipeline
- raw → clean → features → viz → (export a `data/processed/`)

El flujo de datos sigue un orden estrictamente secuencial:

- Raw: Carga del CSV original desde data/raw/.

- Clean: Limpieza de nulos, tipado de datos y eliminación de columnas irrelevantes para este análisis (num_expediente, coordenadas).

- Features: Creación de variables derivadas (temporada, grupo_etario, tramo_horario).

- Viz: Generación automática de matrices de correlación y heatmaps temporales.

- Export: El dataset procesado se guarda en data/processed/ para modelos de ML futuros.

### 6) 🔎 Hallazgos
- Insight 1: Concentración Temporal: Los accidentes se disparan en las franjas de entrada/salida laboral (08:00 y 18:00), se concentran más entre los días jueves y viernes. Ir al gráfico: Frecuencia de accidentes por hora y dia de la semana.

- Insight 2: Perfil de Riesgo: Los conductores adultos (30-59 años) presentan una mayor frecuencia de accidentes por "alcance", mientras que para los jóvenes (15-29 años) es la "colisión fronto-lateral". Ir a gráfico: Distribución de tipo de accidente por grupo etario.

- Insight 3: Gravedad por Distrito: Ciertos distritos periféricos muestran una tasa de siniestros mayor, posiblemente vinculada a mayores velocidades de circulación. Ir al gráfico: Top 10 distritos con más accidentes.

### 7) Estructura del proyecto

La lógica se ha modularizado para evitar scripts monolíticos:

- `src/io.py `: Funciones de lectura y escritura de archivos.
 
- `src/cleaning.py `: Lógica de transformación y depuración de tipos.
 
- `src/features.py `: Ingeniería de variables y segmentación.
 
- `src/viz.py `: Funciones de visualización (Seaborn/Matplotlib) con guardado automático.
 
- `main.py `: Orquestador que ejecuta el pipeline completo.

### 8) 🛠️ Cómo ejecutar
- `pip install -r requirements.txt`
- Ejecutar pipeline: `python3 main.py`
- Exploración interactiva (Opcional): Puedes consultar el proceso experimental original abriendo el archivo: `notebooks/eda.ipynb`

### Estructura del proyecto:

```
project_1/
├── main.py
├── data/
│   ├── raw/
│   └── processed/
│   └── images/
├── notebooks/
│   └── eda.ipynb
├── src/
│   ├── __init__.py
│   ├── io.py
│   ├── cleaning.py
│   ├── config.py
│   ├── features.py
│   ├── viz.py
│   └── utils.py
├── README.md
├── .gitignore
└── requirements.txt

```

