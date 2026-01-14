import pandas as pd
import sqlite3

def build_database():
    # 1. Load our fresh CSV files
    print("Loading data from CSV files...")
    prices_df = pd.read_csv('btc_prices_raw.csv')
    sentiment_df = pd.read_csv('sentiment_data_raw.csv')

    # 2. Connect to SQLite (it will create 'crypto_analysis.db' file)
    conn = sqlite3.connect('crypto_analysis.db')
    
    # 3. Save DataFrames to SQL tables
    print("Converting CSVs to SQL tables...")
    prices_df.to_sql('prices', conn, if_exists='replace', index=False)
    sentiment_df.to_sql('sentiment', conn, if_exists='replace', index=False)
    
    # 4. Run a test SQL Query to prove it works
    # We want to see the price on days when people were extremely scared
    print("\nRunning SQL Query: Top 5 'Extreme Fear' days and BTC price...")
    query = """
    SELECT p.Date, p.Close, s.Sentiment_Score, s.Sentiment_Label
    FROM prices p
    JOIN sentiment s ON p.Date = s.Date
    WHERE s.Sentiment_Label = 'Extreme Fear'
    ORDER BY p.Date DESC
    LIMIT 5;
    """
    
    result = pd.read_sql_query(query, conn)
    print(result)
    
    conn.close()
    print("\nDatabase 'crypto_analysis.db' created successfully!")

if __name__ == "__main__":
    build_database()