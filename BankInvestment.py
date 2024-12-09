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
