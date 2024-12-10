from trans_func import Transactions
from Users import User

if __name__ == "__main__":
    # Ask the user if they are an existing user or a new one
    output = input("Are you an existing user? (Yes/No)")
    if output == 'Yes': 
        Name = input("Name: ")
        Surname = input("Surname: ")
        Access = True
        Buy = input("Buy (y is yes): ")
        Sell = input("Sell (y if yes): ")
        user = User(Name,Surname,Access,Buy,Sell)
        AccessType = user.getUserName()
    elif output == 'No':
        Name = input("Name: ")
        Surname = input("Surname: ")
        Access = True
        Buy = input("Buy (y is yes): ")
        Sell = input("Sell (y if yes): ")
        user = User(Name,Surname,Access,Buy,Sell)
        user.newUser()
        AccessType = user.getUserName()
    else: 
        print("The input you gave was wrong.")

    if Access[1] == "Full":
        transactions = Transactions()
        while True:
            action = input("Do you want to buy or sell stocks? (buy/sell/exit): ")
            if action == 'buy':
                stock = input("Enter the stock you want to buy: ")
                amount = int(input("Enter the number of shares you want to buy: "))
                transactions.buy(Access[0],stock,amount)
            elif action == 'sell':
                stock = input("Enter the stock you want to sell: ")
                amount = int(input(f"Enter the number of shares of {stock} you want to sell: "))
                transactions.sell(Access[0],stock,amount)
            elif action == 'exit':
                break
            else:
                print("Invalid option. Please enter 'buy', 'sell', or 'exit'.")
    
    if Access[1] == "Buy":
        transactions = Transactions()
        while True:
            action = input("Do you want to buy? (buy/exit): ")
            if action == 'buy':
                stock = input("Enter the stock you want to buy: ")
                amount = int(input("Enter the number of shares you want to buy: "))
                transactions.buy(Access[0],stock,amount)
            elif action == 'sell':
                print("You don't have the right access to sell stocks.")
            elif action == 'exit':
                break
            else:
                print("Invalid option. Please enter 'buy', or 'exit'.")

    if Access[1] == "Sell":
        transactions = Transactions()
        while True:
            action = input("Do you want to sell? (sell/exit): ")
            if action == 'buy':
                print("You don't have the right access to buy stocks.")
            elif action == 'sell':
                stock = input("Enter the stock you want to sell: ")
                amount = int(input(f"Enter the number of shares of {stock} you want to sell: "))
                transactions.buy(Access[0],stock,amount)
            elif action == 'exit':
                break
            else:
                print("Invalid option. Please enter 'sell', or 'exit'.")   
