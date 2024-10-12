# Python-for-finance
Stock Price Analysis and Financial Metrics Calculation using Python

# Project Overview
This project analyzes historical stock data for Apple Inc. (AAPL), calculates key financial metrics such as daily returns and Simple Moving Averages (SMA), and visualizes the data using line plots and histograms. The objective is to showcase how Python can be used to perform financial data analysis and gain insights into stock trends and volatility.
# Requirements
To run this project, you need to install the following Python libraries:
- pip install yfinance pandas numpy matplotlib

# Files
- main.py: The main script where all the calculations and visualizations take place.
- README.md: Project documentation (this file).
- requirements.txt: A file listing all the dependencies needed to run the project.

# 1. Fetching Stock Data
Using the yfinance library, we fetch one year of historical stock data for Apple Inc. (AAPL). This includes the stock’s daily open, high, low, close, and volume.
# Fetch data for Apple stock for the last 1 year
stock = yf.Ticker("AAPL")
data = stock.history(period="1y")

# Display the first few rows of stock data
print("Apple Stock Data (First 5 Rows):")
print(data.head())

- Stock Data Columns:
- Open: The opening price of the stock on a given day.
- High: The highest price during the day.
- Low: The lowest price during the day.
- Close: The closing price of the stock for the day.
- Volume: The number of shares traded.
- Dividends: Dividends distributed (if any) on that date.

  # 2. Calculating Daily Returns
 <br> Description <br>
  Daily returns represent the percentage change in the stock’s closing price from one day to the next. It helps in understanding how volatile the stock is over a given period.
# Calculate daily returns
data['Daily Return'] = data['Close'].pct_change()

# Display first 5 rows of daily returns
print("\nApple Stock Daily Returns (First 5 Rows):")
print(data[['Close', 'Daily Return']].head())

<br>Formula:<br>
Daily Return =Close𝑡−Close𝑡−1Close𝑡−1
Daily Return= Close t−1Close t −Close t−1 
Explanation: This calculation shows the percentage increase or decrease in the stock’s closing price compared to the previous day.

# 3. Calculating Simple Moving Averages (SMA)
<br>Description<br>
A Simple Moving Average (SMA) is the average of the stock's closing price over a certain number of days. In this project, we calculate both the 20-day SMA and 50-day SMA to observe short-term and long-term trends in the stock price
# Calculate 20-day and 50-day Simple Moving Averages (SMA)
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Display SMAs
print("\nApple Stock Simple Moving Averages (First 5 Rows):")
print(data[['Close', 'SMA_20', 'SMA_50']].head())
![Capture](https://github.com/user-attachments/assets/6f2e7c8c-2862-46f1-ae40-238a5b88ce55)

# 4. Visualizing Stock Prices and Moving Averages\
<br>Description<br>
We visualize the closing stock prices along with the 20-day and 50-day SMAs using Matplotlib. This helps to observe how the stock price behaves in relation to its short-term and long-term averages.
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='AAPL Close Price', color='blue')
plt.plot(data['SMA_20'], label='20-Day SMA', color='orange')
plt.plot(data['SMA_50'], label='50-Day SMA', color='green')
plt.title('AAPL Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()
<br>Purpose:<br> This visualization helps in understanding price trends, spotting crossovers between short-term and long-term averages, and identifying potential buy/sell signals.

# 5. Visualizing Daily Returns
<br>Description<br>
We plot a histogram of the daily returns to visualize their distribution. This provides insights into the stock’s volatility and the range of daily price movements.
plt.figure(figsize=(10,6))
plt.hist(data['Daily Return'].dropna(), bins=50, alpha=0.75, color='blue')
plt.title('AAPL Daily Returns Distribution')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.show()

<br>Purpose:<br> The histogram illustrates the distribution of the stock's daily returns, which helps assess the risk and volatility of the stock.

# 6. Conclusion
This project demonstrates how Python can be used for basic financial data analysis, covering data extraction, manipulation, and visualization. By calculating daily returns and moving averages, we gain valuable insights into the stock's performance and volatility.

