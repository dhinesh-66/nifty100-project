import pandas as pd

class DataValidator:

    def __init__(self):
        self.failures = []

    def add_failure(self, rule, severity, company, year, message):
        self.failures.append({
            "rule": rule,
            "severity": severity,
            "company": company,
            "year": year,
            "message": message
        })

    def dq01_pk_uniqueness(self, df, table_name):
        duplicates = df[df["id"].duplicated()]

        for _, row in duplicates.iterrows():
            self.add_failure(
                "DQ-01",
                "CRITICAL",
                row.get("company_id", "N/A"),
                row.get("year", "N/A"),
                f"Duplicate ID in {table_name}"
            )

    def dq02_company_year_uniqueness(self, df, table_name):
        if "company_id" in df.columns and "year" in df.columns:

            duplicates = df[
                df.duplicated(
                    subset=["company_id", "year"],
                    keep=False
                )
            ]

            for _, row in duplicates.iterrows():
                self.add_failure(
                    "DQ-02",
                    "CRITICAL",
                    row["company_id"],
                    row["year"],
                    f"Duplicate company-year in {table_name}"
                )

    def dq06_positive_sales(self, profit_df):
        bad_rows = profit_df[profit_df["sales"] <= 0]

        for _, row in bad_rows.iterrows():
            self.add_failure(
                "DQ-06",
                "WARNING",
                row["company_id"],
                row["year"],
                "Sales value <= 0"
            )

    def export_failures(self):
        pd.DataFrame(self.failures).to_csv(
            "output/validation_failures.csv",
            index=False
        )