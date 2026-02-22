from src.config import RAW_PATH
from src.io import load_csv, save_processed
from src.cleaning import clean
from src.features import build_features
from src.utils import assert_columns, memory_saving
from src.viz import plot_graph


def main():
    df_raw = load_csv(RAW_PATH)
    df = clean(df_raw)
    memory_saving(df_raw,df)
    df = build_features(df)
    assert_columns(df, ['fecha_hora', 'distrito', 'tipo_accidente', 'estado_meteorológico', 'tipo_vehiculo', 'tipo_persona', 'rango_edad', 'sexo', 'positiva_alcohol',
       'positiva_droga', 'mes', 'dia_semana', 'hora', 'temporada', 'pct_alcohol_por_distrito', 'grupo_etario'])

    plot_graph(df)
    
    save_processed(df,'data/processed/clean_df.csv')


if __name__ == "__main__":
    main()
