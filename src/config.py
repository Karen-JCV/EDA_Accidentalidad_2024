from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RAW_PATH = ROOT / "data" / "raw" / "2024_Accidentalidad.csv"
OUT_PATH = ROOT / "data" / "processed" / "clean_2024_Accidentalidad.csv"