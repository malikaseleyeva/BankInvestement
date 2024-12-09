from trans_func import Transactions

if __name__ == "__main__":
    transactions = Transactions()
    while True:
        action = input("Do you want to buy or sell stocks? (buy/sell/exit): ")
        if action == 'buy':
            transactions.buy('malika')
        elif action == 'sell':
            transactions.sell('malika')
        elif action == 'exit':
            break
        else:
            print("Invalid option. Please enter 'buy', 'sell', or 'exit'.")
