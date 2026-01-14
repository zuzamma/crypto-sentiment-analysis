import sqlite3
import pandas as pd

def export_data():
    conn = sqlite3.connect('crypto_analysis.db')
    # Łączymy dane w jedną tabelę (Master Table)
    query = """
    SELECT p.Date, p.Open, p.High, p.Low, p.Close, p.Volume, 
           s.Sentiment_Score, s.Sentiment_Label
    FROM prices p
    JOIN sentiment s ON p.Date = s.Date
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # Zapisujemy jako finalny plik do Power BI
    df.to_csv('final_crypto_data.csv', index=False)
    print("Export successful! Use 'final_crypto_data.csv' in Power BI.")

if __name__ == "__main__":
    export_data()