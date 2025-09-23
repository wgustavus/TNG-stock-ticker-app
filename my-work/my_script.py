# %% [markdown]
# ### Sep 2025 - Zach Wilson DataExpert BEGINNER Bootcamp
#  DATA PIPELINE 'intro' video -- makes a pipeline from stock ticker via API script
#  NOTES: 
#    - Requires Polygon.AI free account (https://polygon.io/)
#    - Best practice = store API key in .env file
#    - Best practice = store required libraries in a requirements.txt file (use to install: pip install -r requirements.txt)

# %%
import time
import requests
import csv
import os
from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

LIMIT = 1000


# %%
# define the stock job using MY code lab-lecture scratch (rather than Zach's script.py)

def run_stock_job():
    url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}'
    response = requests.get(url)
    tickers = []

    data = response.json()
    for ticker in data['results']:
        tickers.append(ticker)

    while 'next_url' in data:
        print('requesting next page', data['next_url'])
        response = requests.get(data['next_url'] + f'&apiKey={POLYGON_API_KEY}')
        data = response.json()
        # Must add rate limiter to use my free API key to avoid errors
        time.sleep(14)
        print(data)
        for ticker in data['results']:
            tickers.append(ticker)

    example_ticker =  {'ticker': 'ZWS', 
        'name': 'Zurn Elkay Water Solutions Corporation', 
        'market': 'stocks', 
        'locale': 'us', 
        'primary_exchange': 'XNYS', 
        'type': 'CS', 
        'active': True, 
        'currency_name': 'usd', 
        'cik': '0001439288', 
        'composite_figi': 'BBG000H8R0N8', 	'share_class_figi': 'BBG001T36GB5', 	'last_updated_utc': '2025-09-11T06:11:10.586204443Z'}

    # Write tickers to CSV with example_ticker schema
    fieldnames = list(example_ticker.keys())
    output_csv = 'tickers.csv'
    with open(output_csv, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for t in tickers:
            row = {key: t.get(key, '') for key in fieldnames}
            writer.writerow(row)
    print(f'Wrote {len(tickers)} rows to {output_csv}')

if __name__ == '__main__':
    run_stock_job()












