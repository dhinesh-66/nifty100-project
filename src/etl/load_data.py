import sqlite3
import pandas as pd
from src.etl.loader import load_excel

# Connect to SQLite
conn = sqlite3.connect("db/nifty100.db")

# Mapping: Excel file -> SQLite table
files = {
    "companies.xlsx": "companies",
    "profitandloss.xlsx": "profitandloss",
    "balancesheet.xlsx": "balancesheet",
    "cashflow.xlsx": "cashflow",
    "analysis.xlsx": "analysis",
    "documents.xlsx": "documents",
    "prosandcons.xlsx": "prosandcons",
    "sectors.xlsx": "sectors",
    "stock_prices.xlsx": "stock_prices",
    "financial_ratios.xlsx": "financial_ratios",
    "peer_groups.xlsx": "peer_groups",
    "market_cap.xlsx": "market_cap"
}

audit = []

for file_name, table_name in files.items():
    print(f"Loading {file_name}...")

    df = load_excel(f"data/raw/{file_name}")

    rows = len(df)

    df.to_sql(
        table_name,
        conn,
        if_exists="append",
        index=False
    )

    audit.append({
        "table": table_name,
        "rows_loaded": rows,
        "status": "SUCCESS"
    })

# Save audit report
audit_df = pd.DataFrame(audit)
audit_df.to_csv("output/load_audit.csv", index=False)

conn.commit()
conn.close()

print("\nAll datasets loaded successfully!")
print("load_audit.csv generated.")