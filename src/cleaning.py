import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()
    # 1. Eliminar columnas que no aportan al análisis
    cols_to_drop = ['num_expediente', 'localizacion', 'numero', 'cod_distrito', 'cod_lesividad', 'lesividad', 'coordenada_x_utm', 'coordenada_y_utm']
    df_clean.drop(columns=[c for c in cols_to_drop if c in df_clean.columns], errors='ignore')
    
    # 2. Eliminar posibles espacios o caracteres especiales en el nombre de las variables. Estandarizar.
    df_clean.columns = [c.strip().lower().replace(' ', '_') for c in df_clean.columns]

    # 3. Eliminar observaciones/filas duplicadas.
    df_clean = df_clean.drop_duplicates()
    
    # 4. Conversión de fecha y hora / Variables bool
    df_clean['fecha'] = pd.to_datetime(df_clean['fecha'], errors='coerce', dayfirst=True)
    df_clean['hora'] = pd.to_datetime(df_clean['hora'], format="%H:%M:%S", errors='coerce')
    df_clean['positiva_alcohol'] = (df_clean['positiva_alcohol'].map({'S':True, 'N': False}).fillna(False).astype("bool"))
    df_clean['positiva_droga'] = (df_clean['positiva_droga'].fillna(0)).astype('bool')
    
    #Agregar variable 'fecha_hora' de tipo datetime y eliminar variables separadas 'fecha' y 'hora'.
    df_clean.insert(0, 'fecha_hora',
                    df_clean['fecha'] + (df_clean['hora'] - df_clean['hora'].dt.normalize()))
    df_clean = df_clean.drop(columns=['fecha', 'hora'], errors="ignore")

    # Unificar criterio de observaciones/filas localizadas con diferentes sinónimos para "Desconocido" en el dataset por "unknown".
    df_clean['estado_meteorológico'] = df_clean['estado_meteorológico'].astype('string').str.strip().str.lower().replace({'se desconoce': 'unknown'})
    df_clean['rango_edad'] = df_clean['rango_edad'].astype('string').str.strip().str.lower().replace({'desconocido': 'unknown', 'más de 74 años': 'mayor a 74 años', 'menor de 5 años': 'menor a 5 años'})
    df_clean['sexo'] = df_clean['sexo'].astype('string').str.strip().str.lower().replace({'desconocido': 'unknown'})

    # Imputación en tres variables categóricas que representan porcentajes bajos de valores nulos por 'unknown', se evita imputación con la moda por tratarse de categorias importantes y de impacto.
    df_clean[['tipo_accidente', 'estado_meteorológico', 'tipo_vehiculo']] = df_clean[['tipo_accidente', 'estado_meteorológico', 'tipo_vehiculo']].fillna('unknown')
    
    # Modificar tipo de dato de str/object a categoria para el ahorro de memoria.
    columnas_categoria = [
        "distrito",
        "tipo_accidente",
        "estado_meteorológico",
        "tipo_vehiculo",
        "tipo_persona",
        "rango_edad",
        "sexo"
    ]
    df_clean[columnas_categoria] = df_clean[columnas_categoria].astype("category")
    return df_clean