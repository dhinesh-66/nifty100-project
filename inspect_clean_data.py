from src.etl.loader import load_excel

files = [
    "companies.xlsx",
    "profitandloss.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx"
]

for file in files:
    df = load_excel(f"data/raw/{file}")

    print("\n" + "="*60)
    print(file)
    print("="*60)

    print(df.head())
    print("\nColumns:")
    print(df.columns.tolist())
    