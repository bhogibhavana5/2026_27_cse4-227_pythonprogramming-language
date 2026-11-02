Multi-Currency Travel Budget Analysis
1. Problem Statement
Develop a Python program to analyze travel expenses incurred in multiple currencies. The program should convert all expenses into a common base currency using the supplied exchange rates, incorporate currency conversion fees, compare the total planned spending against a specified budget, and identify the largest expense category.

The program should display the converted expenses, conversion fees, total spending, budget status, and the category with the highest expense.
2. Algorithm
1. Start the program.
2. Read the base currency and travel budget.
3. Read the number of expense categories.
4. For each expense category:
   - Read the category name.
   - Read the expense amount.
   - Read the original currency.
   - Read the exchange rate to the base currency.
   - Read the conversion fee percentage.
5. Calculate the converted expense.
\[
\text{Converted Amount}=\text{Expense}\times\text{Exchange Rate}
\]

6. Calculate the conversion fee.
\[
\text{Fee}=\frac{\text{Converted Amount}\times\text{Fee Percentage}}{100}
\]

7. Calculate the total expense including fees.
\[
\text{Total Expense}=\text{Converted Amount}+\text{Fee}
\]

8. Add all expenses to calculate total travel spending.
9. Identify the largest expense category.
10. Compare total spending with the budget.
11. Display the expense report and budget status.
12. Stop.
3. Flowchart
~~~mermaid

flowchart TD
    A([Start]) --> B[/Input base currency and budget/]
    B --> C[/Input number of categories/]
    C --> D[Set total spending = 0]
    D --> E[/Input category and expense details/]
    E --> F[Calculate converted amount]
    F --> G[Calculate conversion fee]
    G --> H[Calculate total expense]
    H --> I[Update total spending]
    I --> J{All categories processed?}
    J -- No --> E
    J -- Yes --> K[Find largest expense category]
    K --> L{Total spending <= Budget?}
    L -- Yes --> M[Calculate remaining budget]
    L -- No --> N[Calculate exceeded amount]
    M --> O[Display expense report]
    N --> O
    O --> P([Stop])

~~~

5. Sample Input

Enter base currency: INR
Enter travel budget: 90000
Enter number of expense categories: 4

Expense Category 1
Enter category name: Accommodation
Enter expense amount: 500
Enter original currency: USD
Enter exchange rate: 83
Enter conversion fee percentage: 2

Expense Category 2
Enter category name: Food
Enter expense amount: 200
Enter original currency: EUR
Enter exchange rate: 90
Enter conversion fee percentage: 1.5

Expense Category 3
Enter category name: Transport
Enter expense amount: 150
Enter original currency: GBP
Enter exchange rate: 105
Enter conversion fee percentage: 2

Expense Category 4
Enter category name: Activities
Enter expense amount: 100
Enter original currency: USD
Enter exchange rate: 83
Enter conversion fee percentage: 2



6. Sample Output

========== TRAVEL BUDGET REPORT ==========
Base Currency: INR

Category-wise Expenses:

Category: Accommodation
Original Expense: 500.00 USD
Converted Amount: 41500.00 INR
Conversion Fee: 830.00 INR
Total Expense: 42330.00 INR

Category: Food
Original Expense: 200.00 EUR
Converted Amount: 18000.00 INR
Conversion Fee: 270.00 INR
Total Expense: 18270.00 INR

Category: Transport
Original Expense: 150.00 GBP
Converted Amount: 15750.00 INR
Conversion Fee: 315.00 INR
Total Expense: 16065.00 INR

Category: Activities
Original Expense: 100.00 USD
Converted Amount: 8300.00 INR
Conversion Fee: 166.00 INR
Total Expense: 8466.00 INR

Total Travel Spending: 85131.00 INR
Travel Budget: 90000.00 INR

Largest Expense Category: Accommodation
Largest Expense Amount: 42330.00 INR

Status: Within Budget
Remaining Budget: 4869.00 INR




8. Result
The program successfully:
- Converts travel expenses from USD, EUR, GBP, and other currencies into INR.
- Calculates currency conversion fees.
- Computes the total travel spending.
- Identifies the largest expense category.
- Checks whether the spending is within the budget.
- Displays the remaining budget or exceeded amount.
The program is suitable for Python programming practicals and academic assignments.
