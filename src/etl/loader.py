# src/etl/loader.py

import pandas as pd


def load_excel(file_path):
    """
    Load an Excel file into a dataframe.
    """

    try:
        df = pd.read_excel(file_path)
        print(f"Loaded {file_path}")
        print(df.shape)

        return df

    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None