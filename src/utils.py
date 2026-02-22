import pandas as pd
def assert_columns(df: pd.DataFrame, required: list[str]) -> None:
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f'Missing columns: {missing}')

def memory_saving(df_antes, df_despues):
    """
    Calcula y muestra el ahorro de memoria tras la optimización de tipos de datos.
    """
    mem_antes = df_antes.memory_usage(deep=True).sum()
    mem_despues = df_despues.memory_usage(deep=True).sum()
    
    ahorro = (mem_antes - mem_despues) / mem_antes * 100
    
    print("\n" + "="*30)
    print("📊 REPORTE DE MEMORIA")
    print("="*30)
    print(f"Memoria Original:  {mem_antes / 1024**2:.2f} MB")
    print(f"Memoria Optimizada: {mem_despues / 1024**2:.2f} MB")
    print(f"Ahorro Total:       {ahorro:.2f}%")
    print("="*30 + "\n")
    
    return ahorro