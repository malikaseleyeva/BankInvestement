from trans_func import Transactions
from Users import newUser, getUserName

if __name__ == "__main__":
    # Ask the user if they are an existing user or a new one
    output = input("Are you an existing user? (Yes/No)")
    if output == 'Yes': 
        Access = getUserName()
    elif output == 'No':
        newUser()
        Access = getUserName()
    else: 
        print("The input you gave was wrong.")

    if Access[1] == "Full":
        transactions = Transactions()
        while True:
            action = input("Do you want to buy or sell stocks? (buy/sell/exit): ")
            if action == 'buy':
                transactions.buy(Access[0])
            elif action == 'sell':
                transactions.sell(Access[0])
            elif action == 'exit':
                break
            else:
                print("Invalid option. Please enter 'buy', 'sell', or 'exit'.")
    
    if Access[1] == "Buy":
        transactions = Transactions()
        while True:
            action = input("Do you want to buy? (buy/exit): ")
            if action == 'buy':
                transactions.buy(Access[0])
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
                transactions.buy(Access[0])
            elif action == 'exit':
                break
            else:
                print("Invalid option. Please enter 'sell', or 'exit'.")   