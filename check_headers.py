import pandas as pd

files = [
    "companies.xlsx",
    "profitandloss.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx"
]

for file in files:
    print("\n" + "="*60)
    print(file)
    print("="*60)

    df = pd.read_excel(f"data/raw/{file}", header=None)

    print(df.head(10))