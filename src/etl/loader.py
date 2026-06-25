import pandas as pd
import os

SPECIAL_FILES = [
    "companies.xlsx",
    "profitandloss.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx",
    "analysis.xlsx",
    "documents.xlsx",
    "prosandcons.xlsx"
]

def load_excel(file_path):
    file_name = os.path.basename(file_path)

    if file_name in SPECIAL_FILES:
        return pd.read_excel(file_path, header=1)

    return pd.read_excel(file_path)