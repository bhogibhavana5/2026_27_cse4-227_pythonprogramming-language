Multi-Currency Travel Budget Analysis
1. Problem Statement
Develop a Python program to analyze travel expenses incurred in multiple currencies.

The program should:
- Accept travel expenses from different categories such as food, hotel, transport, and shopping.
- Convert each expense into the base currency using the supplied exchange rates.
- Calculate currency conversion fees.
- Compute the total travel expenditure.
- Compare the total expenditure against the planned travel budget.
- Identify the largest expense category.
- Determine whether the traveler is within the budget or has exceeded it.
2. Algorithm
1. Start the program.
2. Read the total travel budget in the base currency.
3. Read the number of expense entries.
4. For each expense:
   - Read the expense category.
   - Read the amount spent.
   - Read the currency code.
   - Read the exchange rate to the base currency.
   - Read the conversion fee percentage.
   - Calculate the converted amount.
   - Calculate the conversion fee.
   - Calculate the total expense including fee.
   - Add the expense to the category total.
5. Calculate the total travel expenditure.
6. Compare the expenditure with the budget.
7. Identify the category with the highest expense.
8. Display the itemized expense report.
9. Display the budget status and largest expense category.
10. Stop.
3. Flowchart
~~~mermaid
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

~~~


5. Sample Input

Enter travel budget in INR: 40000
Enter number of expenses: 4

Enter expense details:

Expense 1
Enter expense category: Hotel
Enter amount spent: 200
Enter currency code: USD
Enter exchange rate to INR: 83
Enter conversion fee percentage: 2

Expense 2
Enter expense category: Food
Enter amount spent: 100
Enter currency code: EUR
Enter exchange rate to INR: 90
Enter conversion fee percentage: 1

Expense 3
Enter expense category: Transport
Enter amount spent: 50
Enter currency code: GBP
Enter exchange rate to INR: 105
Enter conversion fee percentage: 1.5

Expense 4
Enter expense category: Shopping
Enter amount spent: 100
Enter currency code: USD
Enter exchange rate to INR: 83
Enter conversion fee percentage: 2



6. Sample Output

Converted Amount: INR 16600.00
Conversion Fee: INR 332.00
Total Expense: INR 16932.00

Converted Amount: INR 9000.00
Conversion Fee: INR 90.00
Total Expense: INR 9090.00

Converted Amount: INR 5250.00
Conversion Fee: INR 78.75
Total Expense: INR 5328.75

Converted Amount: INR 8300.00
Conversion Fee: INR 166.00
Total Expense: INR 8466.00

========== TRAVEL BUDGET REPORT ==========
Travel Budget       : INR 40000.00
Total Expenditure   : INR 39816.75

Category-wise Expenses:
Hotel          : INR 16932.00
Food           : INR 9090.00
Transport      : INR 5328.75
Shopping       : INR 8466.00

Largest Expense Category: Hotel
Largest Category Amount : INR 16932.00

Status: Within Budget
Remaining Budget: INR 183.25
=========================================







Result
The program successfully converts expenses from USD, EUR, and GBP into INR using supplied exchange rates, adds conversion fees, calculates the total expenditure, identifies Hotel as the largest expense category, and determines that the traveler is within the budget of ₹40,





Ads do not influence the answers you get from ChatGPT. Your chats stay private. Learn about ads and personalization
