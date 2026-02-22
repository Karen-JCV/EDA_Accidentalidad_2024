import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    # Generar copia del dataset limpio para agregar variables temporales y transformaciones
    df_features = df.copy()

    # Variables Temporales
    df_features['mes'] = df_features['fecha_hora'].dt.month
    df_features['dia_semana'] = df_features['fecha_hora'].dt.day_name()
    df_features['hora'] = df_features['fecha_hora'].dt.hour

    ## Variable que permita analizar patrones de riesgo por época del año.
    def asignar_temporada(mes):
        if mes in [12, 1, 2]:
            return 'invierno'
        elif mes in [3, 4, 5]:
            return 'primavera'
        elif mes in [6, 7, 8]:
            return 'verano'
        elif mes in [9, 10, 11]:
            return 'otoño'
        else:
            return 'unknown'

    df_features['temporada'] = df_features['mes'].apply(asignar_temporada)

    ## Calcular porcentaje de accidentes con alcohol positivo por distrito
    pct_alcohol = (
        df_features.groupby('distrito')['positiva_alcohol']
          .mean()                           # obtiene la media → proporción de True
          .mul(100)                         # convierte a porcentaje
          .round(2)                         # redondea a 2 decimales
    )

    # Inicializar en 0
    df_features['pct_alcohol_por_distrito'] = 0.0

    # Asignar porcentaje sólo a los True
    df_features.loc[df_features['positiva_alcohol'] == True,
                    'pct_alcohol_por_distrito'] = (
        df_features['distrito'].map(pct_alcohol)
    )

    ## Variable que permita contrastar si ciertos grupos etarios presentan más riesgo con drogas o alcohol. 
    # Definir el mapeo de rangos originales a categorías simplificadas
    mapa_grupo_etario = {
        'menor a 5 años': 'niños',
        'de 6 a 9 años': 'niños',
        'de 10 a 14 años': 'niños',
        'de 15 a 17 años': 'jóvenes',
        'de 18 a 20 años': 'jóvenes',
        'de 21 a 24 años': 'jóvenes',
        'de 25 a 29 años': 'jóvenes',
        'de 30 a 34 años': 'adultos',
        'de 35 a 39 años': 'adultos',
        'de 40 a 44 años': 'adultos',
        'de 45 a 49 años': 'adultos',
        'de 50 a 54 años': 'adultos',
        'de 55 a 59 años': 'adultos',
        'de 60 a 64 años': 'adultos',
        'de 65 a 69 años': 'mayores',
        'de 70 a 74 años': 'mayores',
        'mayor a 74 años': 'mayores',
        'unknown': 'unknown'
    }
    # Aplicar el mapeo
    df_features['grupo_etario'] = df_features['rango_edad'].map(mapa_grupo_etario)

    # Convertir a tipo categoría
    df_features['grupo_etario'] = df_features['grupo_etario'].astype('category')
    return df_features