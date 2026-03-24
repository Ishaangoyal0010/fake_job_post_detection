import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """Load raw CSV data from the given filepath."""
    df = pd.read_csv(filepath)
    print(f"[data_ingestion] Loaded data: {df.shape[0]} rows, {df.shape[1]} cols")
    return df
