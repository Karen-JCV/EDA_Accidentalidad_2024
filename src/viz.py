import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_graph(df: pd.DataFrame, output_folder='data/images/' ) -> None:
    # Gráfico 1: Distribución de accidentes por hora del día — Histograma numérico
    plt.figure(figsize=(8,4))
    sns.histplot(df['hora'], bins=24, color='darkorange')
    plt.title("Distribución de accidentes por hora del día")
    plt.xlabel("Hora")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig(f"{output_folder}Distribución_accidentes_por_hora.png")
    plt.close()

    # Gráfico 2: Boxplot del porcentaje de alcohol positivo por distrito — Boxplot numérico/categórico
    plt.figure(figsize=(12,6))
    sns.boxplot(data=df, x='distrito', y='pct_alcohol_por_distrito', color='lightcoral')
    plt.title("% de accidentes con alcohol positivo por distrito")
    plt.xlabel("Distrito")
    plt.ylabel("Porcentaje de alcohol positivo")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f"{output_folder}Ptc_accidentes_con_alcohol_positivo_por_distrito.png")
    plt.close()

    # Gráfico 3: Distribución de accidentes por distrito top 10 — Barras verticales
    plt.figure(figsize=(10,5))
    df['distrito'].value_counts().head(10).plot(kind='bar', color='steelblue')
    plt.title("Top 10 distritos con más accidentes")
    plt.xlabel("Distrito")
    plt.ylabel("Número de accidentes")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f"{output_folder}Top_10_distritos_con_mas_accidentes.png")
    plt.close()

    # Gráfico 4: Proporción de accidentes por temporada — Gráfico de pastel
    plt.figure(figsize=(6,6))
    df['temporada'].value_counts().plot(
        kind='pie', autopct='%1.1f%%', startangle=90, cmap='Pastel2'
    )
    plt.ylabel('')
    plt.title("Proporción de accidentes por temporada")
    plt.tight_layout()
    plt.savefig(f"{output_folder}Proporcion_de_accidentes_por_temporada.png")
    plt.close()

    # Gráfico 5: Comparativa alcohol y droga por grupo etario — Barras lado a lado
    comp = (
        df.groupby('grupo_etario')[['positiva_alcohol','positiva_droga']]
          .mean().mul(100).round(2)
          .reset_index()
    )
    plt.figure(figsize=(8,5))
    x = range(len(comp))
    plt.bar(x, comp['positiva_alcohol'], width=0.4, label='Alcohol +', color='tomato')
    plt.bar([i + 0.4 for i in x], comp['positiva_droga'], width=0.4, label='Droga +', color='teal')
    plt.xticks([i + 0.2 for i in x], comp['grupo_etario'])
    plt.title("Porcentaje de positivos (alcohol/droga) por grupo etario")
    plt.xlabel("Grupo etario")
    plt.ylabel("Porcentaje (%)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_folder}Pct_de_positivos_alcohol_droga_por_grupo_etario.png")
    plt.close()

    # Gráfico 6: Accidentes por grupo etario y tipo de accidente — Gráfico de barras agrupadas
    plt.figure(figsize=(12,6))
    sns.countplot(data=df, x='grupo_etario', hue='tipo_accidente', 
                  order=['niños','jóvenes','adultos','mayores'], palette='tab10')
    plt.title("Distribución de tipo de accidente por grupo etario")
    plt.xlabel("Grupo etario")
    plt.ylabel("Número de accidentes")
    plt.legend(title='Tipo de accidente', bbox_to_anchor=(1.05,1))
    plt.tight_layout()
    plt.savefig(f"{output_folder}Distribucion_de_tipo_de_accidente_por_grupo_etario.png")
    plt.close()

    # Gráfico 7: Matriz de correlaciones numéricas — Heatmap global de correlación
    plt.figure(figsize=(6,6))
    sns.heatmap(df.select_dtypes('number').corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Matriz de correlaciones numéricas")
    plt.tight_layout()
    plt.savefig(f"{output_folder}Matriz_de_correlaciones_numéricas.png")
    plt.close()

    # Gráfico 8: Mapa de calor (heatmap) de hora vs día de la semana — Cruce temporal de dos variables categóricas
    pivot_hora_dia = df.pivot_table(index='dia_semana', columns='hora', 
                                             values='distrito', aggfunc='count')
    plt.figure(figsize=(12,6))
    sns.heatmap(pivot_hora_dia, cmap='YlOrRd')
    plt.title("Frecuencia de accidentes por hora y día de la semana")
    plt.xlabel("Hora del día")
    plt.ylabel("Día de la semana")
    plt.tight_layout()
    plt.savefig(f"{output_folder}Frecuencia_de_accidentes_por_hora_y_dia_de_la_semana.png")
    plt.close()


