# src/etl/normaliser.py

import re

def normalize_year(year):
    """
    Convert different year formats to a standard integer year.
    """

    if year is None:
        return None

    year = str(year).strip()

    # FY23 -> 2023
    if re.match(r"FY\d{2}$", year):
        return int("20" + year[-2:])

    # 23 -> 2023
    if re.match(r"^\d{2}$", year):
        return int("20" + year)

    # 2023-24 -> 2023
    if re.match(r"^\d{4}-\d{2}$", year):
        return int(year[:4])

    # 2023 -> 2023
    if re.match(r"^\d{4}$", year):
        return int(year)

    return None


def normalize_ticker(ticker):
    """
    Standardize stock ticker format.
    """

    if ticker is None:
        return None

    ticker = str(ticker).strip().upper()

    ticker = ticker.replace(".NS", "")
    ticker = ticker.replace(".BO", "")

    return ticker