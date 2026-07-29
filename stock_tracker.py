import os

def stock_portfolio_tracker():
    # Hardcoded stock prices dictionary
    stock_prices = {
        'AAPL': 180,
        'TSLA': 250,
        'GOOGL': 140,
        'AMZN': 175,
        'MSFT': 400
    }

    portfolio = {}
    total_portfolio_value = 0

    print("=" * 40)
    print("   WELCOME TO STOCK PORTFOLIO TRACKER   ")
    print("=" * 40)
    print("\nAvailable Stocks & Prices (USD):")
    for stock, price in stock_prices.items():
        print(f" - {stock}: ${price}")

    print("\n" + "-" * 40)

    # Getting input from user
    while True:
        stock_name = input("Enter Stock Name (e.g. AAPL) or type 'done' to finish: ").strip().upper()
        
        if stock_name == 'DONE':
            break

        if stock_name not in stock_prices:
            print("Invalid stock! Please choose from the available list above.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.\n")
                continue
        except ValueError:
            print("Please enter a valid number for quantity.\n")
            continue

        # Add or update portfolio
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"Added {quantity} shares of {stock_name} to portfolio.\n")

    # Display Summary
    if not portfolio:
        print("\nNo stocks added to portfolio.")
        return

    print("\n" + "=" * 40)
    print("         YOUR PORTFOLIO SUMMARY         ")
    print("=" * 40)

    summary_text = "Stock\t\tQuantity\tPrice\t\tTotal Value\n"
    summary_text += "-" * 50 + "\n"

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        total_val = qty * price
        total_portfolio_value += total_val
        summary_text += f"{stock}\t\t{qty}\t\t${price}\t\t${total_val}\n"

    summary_text += "-" * 50 + "\n"
    summary_text += f"Total Investment Value: ${total_portfolio_value}\n"

    print(summary_text)

    # Optional: Save result to a file
    save_choice = input("Do you want to save this summary to a text file? (y/n): ").strip().lower()
    if save_choice == 'y':
        file_path = "portfolio_summary.txt"
        with open(file_path, "w") as file:
            file.write(summary_text)
        print(f"Portfolio saved successfully to '{file_path}'!")

if __name__ == "__main__":
    stock_portfolio_tracker()