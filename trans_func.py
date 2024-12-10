import requests
import pandas as pd
from datetime import datetime

class AlphavantageAPI:
    def __init__(self, stock):
        self.url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock}&interval=1min&apikey=JYNTV7BCI77GNKRJ'
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
        self.user_portfolios = {}

    def get_user_portfolio(self, user):
        if user not in self.user_portfolios:
            self.user_portfolios[user] = pd.DataFrame(columns=['Stock', 'Shares', 'Price per Share', 'Total Cost', 'Transaction Date'])
        else:
            self.user_portfolios[user]
        print(self.user_portfolios[user])
    
    def buy(self,user,stock, amount):
        """Buying stock and addding it to the portfolio"""
        self.portfolio_df = self.get_user_portfolio(user)

        api = AlphavantageAPI(stock)
        latest_price = api.get_latest_price()
        total_cost = latest_price * amount
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"The latest price of {stock} is ${latest_price:.2f}")
        print(f"The total cost for {amount} shares of {stock} is ${total_cost:.2f}")

        purchase_data = {
            'Stock': [stock],
            'Shares': [amount],
            'Price per Share': [latest_price],
            'Total Cost': [total_cost],
            'Transaction Date': [current_date]
        }

        purchase_df = pd.DataFrame(purchase_data)
        self.portfolio_df = pd.concat([self.portfolio_df, purchase_df], ignore_index=True)
        
        print("Updated Portfolio after buying:")
        print(self.portfolio_df)
        return self.portfolio_df

    def sell(self,user,stock,amount):
        """Selling of stocks and adding it to the portfolio"""
        self.portfolio_df = self.get_user_portfolio(user)

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
                    'Shares': [-amount],
                    'Price per Share': [latest_price],
                    'Total Cost': [-total_cost],
                    'Transaction Date': [current_date]
                }
                sell_df = pd.DataFrame(sell_data)
                self.portfolio_df = pd.concat([self.portfolio_df, sell_df], ignore_index=True)
                
                print("Updated Portfolio after selling:")
                print(self.portfolio_df)
            else:
                print(f"You are trying to sell more shares than you own. You have {total_shares} shares of {stock}.")
        else:
            print(f"You do not own any shares of {stock}.")
        return self.portfolio_df


if __name__ == "__main__":
    transactions = Transactions()
    while True:
        action = input("Do you want to buy or sell stocks? (buy/sell/exit): ")
        if action == 'buy':
            stock = input("Enter the stock you want to buy: ")
            amount = int(input("Enter the number of shares you want to buy: "))
            transactions.buy('malika',stock,amount)
        elif action == 'sell':
            stock = input("Enter the stock you want to sell: ")
            amount = int(input(f"Enter the number of shares of {stock} you want to sell: "))
            transactions.sell('malika',stock,amount)
        elif action == 'exit':
            break
        else:
            print("Invalid option. Please enter 'buy', 'sell', or 'exit'.")