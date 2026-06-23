from src.etl.normalizer import normalize_year, normalize_ticker


def test_year_fy23():
    assert normalize_year("FY23") == 2023


def test_year_23():
    assert normalize_year("23") == 2023


def test_year_2023():
    assert normalize_year("2023") == 2023


def test_year_range():
    assert normalize_year("2023-24") == 2023


def test_ticker_ns():
    assert normalize_ticker("INFY.NS") == "INFY"


def test_ticker_lower():
    assert normalize_ticker("infy") == "INFY"


def test_ticker_spaces():
    assert normalize_ticker("  tcs  ") == "TCS"