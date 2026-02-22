from pathlib import Path
import pandas as pd


def load_csv(path: str | Path):
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(path, sep=';', encoding='utf-8')

def save_processed(df: pd.DataFrame, path: str):
    """Save a DataFrame into a CSV file."""
    df.to_csv(path, index=False)
    print("Dataframe Saved")