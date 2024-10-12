import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Fetch data for Apple stock for the last 1 year
stock = yf.Ticker("AAPL")
data = stock.history(period="1y")

# Display the first few rows of stock data
print("Apple Stock Data (First 5 Rows):")
print(data.head())

# Step 2: Calculate daily returns
data['Daily Return'] = data['Close'].pct_change()

# Display first 5 rows of daily returns
print("\nApple Stock Daily Returns (First 5 Rows):")
print(data[['Close', 'Daily Return']].head())

# Step 3: Calculate 20-day and 50-day Simple Moving Averages (SMA)
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Display SMAs
print("\nApple Stock Simple Moving Averages (First 5 Rows):")
print(data[['Close', 'SMA_20', 'SMA_50']].head())

# Step 4: Plot stock prices and moving averages
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='AAPL Close Price', color='blue')
plt.plot(data['SMA_20'], label='20-Day SMA', color='orange')
plt.plot(data['SMA_50'], label='50-Day SMA', color='green')
plt.title('AAPL Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Step 5: Visualize daily returns
plt.figure(figsize=(10,6))
plt.hist(data['Daily Return'].dropna(), bins=50, alpha=0.75, color='blue')
plt.title('AAPL Daily Returns Distribution')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.show()

