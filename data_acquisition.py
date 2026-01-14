import yfinance as yf
import requests
import pandas as pd

def get_data():
    print("Downloading BTC price data from Yahoo Finance...")
    btc_data = yf.download('BTC-USD', start='2022-01-01', interval='1d')
    btc_data.reset_index(inplace=True)
    
    print("Downloading sentiment data from Alternative.me API...")
    url = "https://api.alternative.me/fng/?limit=0"
    response = requests.get(url).json()

    fng_data = pd.DataFrame(response['data'])
    fng_data['timestamp'] = pd.to_datetime(fng_data['timestamp'], unit='s')
    fng_data['value'] = fng_data['value'].astype(int)

    fng_data = fng_data[['timestamp', 'value', 'value_classification']]
    fng_data.columns = ['Date', 'Sentiment_Score', 'Sentiment_Label']
    
    btc_data['Date'] = pd.to_datetime(btc_data['Date']).dt.tz_localize(None)
    fng_data['Date'] = pd.to_datetime(fng_data['Date']).dt.tz_localize(None)

    return btc_data, fng_data

if __name__ == "__main__":
    btc, fng = get_data()
    print("\n--- BTC PRICE DATA (First 5 rows) ---")
    print(btc.head())
    print("\n--- SENTIMENT DATA (First 5 rows) ---")
    print(fng.head())
    
    btc.to_csv('btc_prices_raw.csv', index=False)
    fng.to_csv('sentiment_data_raw.csv', index=False)
    print("\nFiles saved as backup CSVs.")