stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")

n = int(input("How many stocks do you own? "))

for i in range(n):
    stock_name = input(f"\nEnter stock {i+1} name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Value of {stock_name}: ${investment}")
    else:
        print("Stock not found in price list!")

print("\n==========================")
print(f"Total Investment Value: ${total_investment}")
print("==========================")

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Result saved to portfolio.txt")
