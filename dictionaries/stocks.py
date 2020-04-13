stockDict = {
    "SPY": "S&P ETF",
    "QQQ": "Nasdaq Composite ETF",
    "AAPL": "Apple Inc",
    "AMZN": "Amazon.com"
}

purchases = [
    ('AAPL', 10000, '11-apr-2009', 13),
    ('AMZN', 5000, '15-dec-2014', 310)
]

for purchase in purchases:
    cost = purchase[1] * purchase[-1]
    ticker = purchase[0]
    company_name = stockDict[ticker]
    print(f"I purchased {company_name} stock for ${cost}")
