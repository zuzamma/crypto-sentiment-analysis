# crypto-sentiment-analysis
# Bitcoin Price vs Market Sentiment Analysis

## Overview
This project explores the relationship between Bitcoin (BTC) price volatility and market psychology using the **Crypto Fear & Greed Index**. It demonstrates a full data pipeline: from API acquisition to SQL storage and visual analysis.

## Project Structure
* `data_acquisition.py`: Fetches BTC price data via `yfinance` and sentiment scores via API.
* `create_database.py`: Stores and joins data in a relational **SQLite** database.
* `analysis_plots.py`: Performs correlation analysis and generates visual insights.
* `crypto_analysis.db`: The final SQL database containing processed records.

## Key Visual Insight
The chart below shows how extreme market emotions often precede price shifts:

![BTC Sentiment Analysis](./price_sentiment_analysis.png)

## Tech Stack
* **Python** (Pandas, Matplotlib, Seaborn)
* **SQL** (SQLite)
* **Financial APIs**
  
## Key Insights
Based on the generated analysis, several patterns were observed:
* **Sentiment as a Leading Indicator:** Significant drops in the Fear & Greed Index (below 20 - Extreme Fear) often preceded local price bottoms, suggesting a potential "buy the dip" opportunity.
* **Correlation:** There is a strong positive correlation between market sentiment and short-term price movements.
* **Greed Peaks:** Periods of "Extreme Greed" (above 80) were frequently followed by price consolidations or corrections, indicating market overheating.
