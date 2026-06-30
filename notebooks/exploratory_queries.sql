-- 1. Total number of companies
SELECT COUNT(*) AS total_companies
FROM companies;

-- 2. List all companies
SELECT id, company_name
FROM companies
ORDER BY company_name;

-- 3. Top 10 companies by market capitalization
SELECT
    c.company_name,
    m.year,
    m.market_cap_crore
FROM market_cap m
JOIN companies c
ON c.id = m.company_id
ORDER BY m.market_cap_crore DESC
LIMIT 10;

-- 4. Companies with highest ROE
SELECT
    company_name,
    roe_percentage
FROM companies
ORDER BY roe_percentage DESC
LIMIT 10;

-- 5. Companies having more than 10 years of Profit & Loss data
SELECT
    company_id,
    COUNT(*) AS total_years
FROM profitandloss
GROUP BY company_id
HAVING COUNT(*) > 10
ORDER BY total_years DESC;

-- 6. Average sales by company
SELECT
    company_id,
    ROUND(AVG(sales),2) AS average_sales
FROM profitandloss
GROUP BY company_id
ORDER BY average_sales DESC
LIMIT 10;

-- 7. Top companies by stock closing price
SELECT
    company_id,
    MAX(close_price) AS highest_close
FROM stock_prices
GROUP BY company_id
ORDER BY highest_close DESC
LIMIT 10;

-- 8. Companies with positive free cash flow
SELECT
    company_id,
    year,
    free_cash_flow_cr
FROM financial_ratios
WHERE free_cash_flow_cr > 0
ORDER BY free_cash_flow_cr DESC
LIMIT 20;

-- 9. Number of companies in each sector
SELECT
    broad_sector,
    COUNT(*) AS companies
FROM sectors
GROUP BY broad_sector
ORDER BY companies DESC;

-- 10. Companies with available annual reports
SELECT
    company_id,
    COUNT(*) AS reports
FROM documents
GROUP BY company_id
ORDER BY reports DESC;