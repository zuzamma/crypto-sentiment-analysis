import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_analysis():
    # 1. Get data from SQL
    conn = sqlite3.connect('crypto_analysis.db')
    query = "SELECT * FROM prices p JOIN sentiment s ON p.Date = s.Date"
    df = pd.read_sql_query(query, conn)
    conn.close()

    # 2. Data Cleaning
    df = df.loc[:,~df.columns.duplicated()]
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Fix for yfinance multi-index columns if they exist
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

    # 3. Create a clean Visualization
    fig, ax1 = plt.subplots(figsize=(14, 7))
    
    # Plotting Price (Left Axis)
    color_price = 'tab:blue'
    ax1.set_xlabel('Date (2022-2026)')
    ax1.set_ylabel('BTC Price (USD)', color=color_price, fontweight='bold')
    ax1.plot(df['Date'], df['Close'], color=color_price, label='BTC Price', linewidth=1.5)
    ax1.tick_params(axis='y', labelcolor=color_price)
    ax1.grid(True, alpha=0.3)

    # Plotting Sentiment (Right Axis)
    ax2 = ax1.twinx()
    color_sent = 'tab:orange'
    ax2.set_ylabel('Fear & Greed Index', color=color_sent, fontweight='bold')
    ax2.plot(df['Date'], df['Sentiment_Score'], color=color_sent, alpha=0.4, label='Sentiment Score')
    ax2.tick_params(axis='y', labelcolor=color_sent)

    plt.title('Bitcoin Price Correlation with Market Sentiment', fontsize=16)
    fig.tight_layout()
    
    # Save the clean plot
    plt.savefig('price_sentiment_analysis.png', dpi=300)
    print("Clean plot saved as 'price_sentiment_analysis.png'")
    plt.show()

if __name__ == "__main__":
    run_analysis()