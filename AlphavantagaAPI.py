import requests
import pandas as pd
from datetime import datetime

class AlphavantageAPI:
    def __init__(self, stock):
        self.url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock}&interval=1min&apikey=53HU7S3992V5RPQZ'
        r = requests.get(self.url, verify=False)
        data = r.json()
        self.data = pd.DataFrame(data['Time Series (1min)']).T  # Transpose to get dates as rows
        self.stock = stock

    def get_latest_price(self):
        latest_date = self.data.index[0]
        latest_price = float(self.data.loc[latest_date]['4. close'])
        return latest_price

class Transactions:
    def __init__(self):
        self.portfolio_df = pd.DataFrame(columns=['Stock', 'Shares', 'Price per Share', 'Total Cost', 'Transaction Date'])

    def buy(self):
        stock = input("Enter the stock you want to buy: ")
        amount = int(input("Enter the number of shares you want to buy: "))
        
        api = AlphavantageAPI(stock)
        latest_price = api.get_latest_price()
        total_cost = latest_price * amount
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
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

        purchase_df = pd.DataFrame(purchase_data)
        self.portfolio_df = pd.concat([self.portfolio_df, purchase_df], ignore_index=True)
        
        print("\nUpdated Portfolio after buying:")
        print(self.portfolio_df)

    def sell(self):
        stock = input("Enter the stock you want to sell: ")
        amount = int(input(f"Enter the number of shares of {stock} you want to sell: "))

        # Check if the stock is in the portfolio and if the amount is sufficient
        if stock in self.portfolio_df['Stock'].values:
            total_shares = self.portfolio_df.loc[self.portfolio_df['Stock'] == stock, 'Shares'].sum()
            if amount <= total_shares:
                api = AlphavantageAPI(stock)
                latest_price = api.get_latest_price()
                total_cost = latest_price * amount
                current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                print(f"The latest price of {stock} is ${latest_price:.2f}")
                print(f"The total amount you receive by selling {amount} shares of {stock} is ${total_cost:.2f}")
                
                # Update the portfolio
                self.portfolio_df.loc[self.portfolio_df['Stock'] == stock, 'Shares'] -= amount
                self.portfolio_df = self.portfolio_df[self.portfolio_df['Shares'] > 0]  # Remove rows where shares are zero
                
                # Add the sale to the portfolio
                sell_data = {
                    'Stock': [stock],
                    'Shares': [-amount],  # Negative because it's a sale
                    'Price per Share': [latest_price],
                    'Total Cost': [-total_cost],
                    'Transaction Date': [current_date]
                }
                sell_df = pd.DataFrame(sell_data)
                self.portfolio_df = pd.concat([self.portfolio_df, sell_df], ignore_index=True)
                
                print("\nUpdated Portfolio after selling:")
                print(self.portfolio_df)
            else:
                print(f"Error: You are trying to sell more shares than you own. You have {total_shares} shares of {stock}.")
        else:
            print(f"Error: You do not own any shares of {stock}.")


if __name__ == "__main__":
    transactions = Transactions()
    while True:
        action = input("Do you want to buy or sell stocks? (buy/sell/exit): ").lower()
        if action == 'buy':
            transactions.buy()
        elif action == 'sell':
            transactions.sell()
        elif action == 'exit':
            break
        else:
            print("Invalid option. Please enter 'buy', 'sell', or 'exit'.")
