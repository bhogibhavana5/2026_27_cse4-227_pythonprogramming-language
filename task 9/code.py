# Multi-Currency Travel Budget Analysis

budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expenses: "))

total_expenses = 0.0
category_totals = {}

print("\nEnter expense details:")

for i in range(n):
    print(f"\nExpense {i + 1}")

    category = input("Enter expense category: ")
    amount = float(input("Enter amount spent: "))
    currency = input("Enter currency code: ")
    exchange_rate = float(input("Enter exchange rate to INR: "))
    fee_percent = float(input("Enter conversion fee percentage: "))

    # Convert expense to INR
    converted_amount = amount * exchange_rate

    # Calculate conversion fee
    conversion_fee = converted_amount * fee_percent / 100

    # Total expense including fee
    final_expense = converted_amount + conversion_fee

    # Update total expenditure
    total_expenses += final_expense

    # Update category expenditure
    if category in category_totals:
        category_totals[category] += final_expense
    else:
        category_totals[category] = final_expense

    print(f"Converted Amount: INR {converted_amount:.2f}")
    print(f"Conversion Fee: INR {conversion_fee:.2f}")
    print(f"Total Expense: INR {final_expense:.2f}")

# Find largest expense category
largest_category = max(category_totals, key=category_totals.get)
largest_amount = category_totals[largest_category]

# Calculate remaining budget
balance = budget - total_expenses

# Display final report
print("\n========== TRAVEL BUDGET REPORT ==========")
print(f"Travel Budget       : INR {budget:.2f}")
print(f"Total Expenditure   : INR {total_expenses:.2f}")

print("\nCategory-wise Expenses:")
for category, amount in category_totals.items():
    print(f"{category:<15}: INR {amount:.2f}")

print(f"\nLargest Expense Category: {largest_category}")
print(f"Largest Category Amount : INR {largest_amount:.2f}")

if total_expenses <= budget:
    print("\nStatus: Within Budget")
    print(f"Remaining Budget: INR {balance:.2f}")
else:
    print("\nStatus: Budget Exceeded")
    print(f"Excess Amount: INR {abs(balance):.2f}")

print("=========================================")

