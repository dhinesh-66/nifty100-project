import sqlite3
import pandas as pd


conn = sqlite3.connect("db/nifty100.db")


print("=" * 60)
print("5 RANDOM COMPANIES")
print("=" * 60)

companies = pd.read_sql("""
SELECT id, company_name
FROM companies
ORDER BY RANDOM()
LIMIT 5;
""", conn)

print(companies)


print("\n" + "=" * 60)
print("YEAR COVERAGE")
print("=" * 60)

coverage = pd.read_sql("""
SELECT
    company_id,
    COUNT(DISTINCT year) AS total_years
FROM profitandloss
GROUP BY company_id
ORDER BY total_years ASC;
""", conn)

print(coverage.head(20))


print("\n" + "=" * 60)
print("COMPANIES WITH LESS THAN 5 YEARS")
print("=" * 60)

few_years = coverage[coverage["total_years"] < 5]

if few_years.empty:
    print("No companies found.")
else:
    print(few_years)

conn.close()