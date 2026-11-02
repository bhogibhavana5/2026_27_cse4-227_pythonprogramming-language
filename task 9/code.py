# Multi-Currency Travel Budget Analysis

base_currency = input("Enter base currency: ").upper()
budget = float(input("Enter travel budget: "))

n = int(input("Enter number of expense categories: "))

expenses = []
total_spending = 0.0

for i in range(n):
    print(f"\nExpense Category {i + 1}")

    category = input("Enter category name: ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter original currency: ").upper()
    exchange_rate = float(input("Enter exchange rate: "))
    fee_percentage = float(input("Enter conversion fee percentage: "))

    # Convert expense into base currency
    converted_amount = amount * exchange_rate

    # Calculate conversion fee
    conversion_fee = converted_amount * fee_percentage / 100

    # Calculate total expense including fee
    total_expense = converted_amount + conversion_fee

    expenses.append({
        "category": category,
        "currency": currency,
        "amount": amount,
        "converted": converted_amount,
        "fee": conversion_fee,
        "total": total_expense
    })

    total_spending += total_expense

# Find the largest expense category
largest_expense = max(expenses, key=lambda x: x["total"])

# Calculate remaining budget
balance = budget - total_spending

# Display expense report
print("\n========== TRAVEL BUDGET REPORT ==========")
print("Base Currency:", base_currency)

print("\nCategory-wise Expenses:")

for expense in expenses:
    print(f"\nCategory: {expense['category']}")
    print(f"Original Expense: {expense['amount']:.2f} "
          f"{expense['currency']}")
    print(f"Converted Amount: {expense['converted']:.2f} "
          f"{base_currency}")
    print(f"Conversion Fee: {expense['fee']:.2f} "
          f"{base_currency}")
    print(f"Total Expense: {expense['total']:.2f} "
          f"{base_currency}")

print("\nTotal Travel Spending:",
      f"{total_spending:.2f} {base_currency}")

print("Travel Budget:",
      f"{budget:.2f} {base_currency}")

print("\nLargest Expense Category:",
      largest_expense["category"])

print("Largest Expense Amount:",
      f"{largest_expense['total']:.2f} {base_currency}")

if total_spending <= budget:
    print("\nStatus: Within Budget")
    print("Remaining Budget:",
          f"{balance:.2f} {base_currency}")
else:
    print("\nStatus: Budget Exceeded")
    print("Exceeded Amount:",
          f"{abs(balance):.2f} {base_currency}")

