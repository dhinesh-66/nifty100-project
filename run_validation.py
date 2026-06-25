from src.etl.loader import load_excel
from src.etl.validator import DataValidator

validator = DataValidator()

companies = load_excel("data/raw/companies.xlsx")
profit = load_excel("data/raw/profitandloss.xlsx")
balance = load_excel("data/raw/balancesheet.xlsx")
cashflow = load_excel("data/raw/cashflow.xlsx")

validator.dq01_pk_uniqueness(companies, "companies")
validator.dq01_pk_uniqueness(profit, "profitandloss")
validator.dq01_pk_uniqueness(balance, "balancesheet")
validator.dq01_pk_uniqueness(cashflow, "cashflow")

validator.dq02_company_year_uniqueness(profit, "profitandloss")
validator.dq02_company_year_uniqueness(balance, "balancesheet")
validator.dq02_company_year_uniqueness(cashflow, "cashflow")

validator.dq06_positive_sales(profit)

validator.export_failures()

print("Validation completed.")