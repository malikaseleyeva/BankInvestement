import requests
import pandas as pd
from datetime import datetime
# make a class for API call 

class AlphavantageAPI:
    """This class is made to make the API call"""
    def __init__(self, stock):
        self.url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey=53HU7S3992V5RPQZ'
        r = requests.get(self.url, verify=False)
        data = r.json()
        self.data = pd.DataFrame(data['Time Series (Daily)']).T  # Transpose to get dates as rows
        self.stock = stock
        # columns = data.columns.tolist()
        # print(data, columns)

    
    def get_latest_price(self):
        latest_date = self.data.index[0]
        latest_price = float(self.data.loc[latest_date]['4. close'])
        return latest_price


def buy():
    stock = input("Enter the stock you want to buy: ")
    amount = int(input("Enter the number of shares you want to buy: "))
    
    api = AlphavantageAPI(stock)
    latest_price = api.get_latest_price()
    total_cost = latest_price * amount
    current_date =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"The latest price of {stock} is ${latest_price:.2f}")
    print(f"The total cost for {amount} shares of {stock} is ${total_cost:.2f}")

    # Create a DataFrame to store the purchase
    purchase_data = {
        'Stock': [stock],
        'Shares': [amount],
        'Price per Share': [latest_price],
        'Total Cost': [total_cost],
        'Transaction Date': [current_date]
    }

    portfolio_df = pd.DataFrame(purchase_data)
    
    print("\nPortfolio:")
    print(portfolio_df)


def sell():
    stock = input("Enter the stock that you want to sell:")
    amount = input(f"Enter the amount of {stock} that you want to sell:")

    api = AlphavantageAPI(stock)
    latest_price = api.get_latest_price()
    total_cost = - latest_price * amount
    current_date =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"The latest price of {stock} is ${latest_price:.2f}")
    print(f"The total amount you receive by selling {amount} shares of {stock} is ${total_cost:.2f}")

    # Create a DataFrame to store sold 
    sell_data = {
        'Stock': [stock],
        'Shares': [amount],
        'Price per Share': [latest_price],
        'Total Cost': [total_cost],
        'Transaction Date': [current_date]
    }

    portfolio_df = pd.DataFrame(sell_data)
    print("\nPortfolio:")
    print(portfolio_df)


def sellorbuy():
    answer = input("Do you want to buy or sell?:")

    if answer == "buy":
        buy()
    elif answer == "sell":
        sell()
    else: 
        print(f"Your answer: {answer} is not being recognized.")