Manufacturing Cost and Profitability Analysis – Python Program
1. Problem Statement
Develop a Python program to calculate the total manufacturing cost and profitability of a product.

The program should calculate:
- Material cost based on quantity and unit price.
- Labour charges based on working hours and hourly rate.
- Material wastage cost based on wastage percentage.
- Machine cost based on machine hours and hourly machine rate.
- Total production cost.
- Selling price and total revenue.
- Profit or loss.
- Profit percentage.
- Whether the production meets the specified profit target.
The program should display a detailed manufacturing cost statement and determine whether the required profit target is achieved.
2. Algorithm
1. Start the program.
2. Read the number of units produced.
3. Input material quantity per unit and material cost per unit.
4. Input labour hours per unit and labour rate per hour.
5. Input wastage percentage.
6. Input machine hours per unit and machine rate per hour.
7. Input selling price per unit.
8. Input the required profit target percentage.
9. Calculate total material cost.
10. Calculate wastage cost.
11. Calculate total labour cost.
12. Calculate total machine cost.
13. Calculate total manufacturing cost.
14. Calculate total revenue.
15. Calculate profit or loss.
16. Calculate profit percentage.
17. Compare the profit percentage with the target percentage.
18. Display the itemized cost statement and profitability result.
19. Stop.
3. Flowchart
 ~~~mermaid

flowchart TD
    A([Start])
    B[/Input production quantity/]
    C[/Input material quantity and rate/]
    D[/Input labour hours and rate/]
    E[/Input wastage percentage/]
    F[/Input machine hours and rate/]
    G[/Input selling price and profit target/]
    H[Calculate material cost]
    I[Calculate wastage cost]
    J[Calculate labour cost]
    K[Calculate machine cost]
    L[Calculate total manufacturing cost]
    M[Calculate total revenue]
    N[Calculate profit or loss]
    O[Calculate profit percentage]
    P{Profit percentage >= target?}
    Q[Display meets profit target]
    R[Display does not meet profit target]
    S[/Display manufacturing cost statement/]
    T([Stop])

    A --> B --> C --> D --> E --> F --> G
    G --> H --> I --> J --> K --> L
    L --> M --> N --> O --> P
    P -->|Yes| Q
    P -->|No| R
    Q --> S
    R --> S
    S --> T

~~~
5. Sample Input

Enter number of units produced: 100
Enter material quantity per unit (kg): 2
Enter material cost per kg (Rs): 50
Enter labour hours per unit: 1.5
Enter labour rate per hour (Rs): 100
Enter wastage percentage: 5
Enter machine hours per unit: 0.5
Enter machine rate per hour (Rs): 200
Enter selling price per unit (Rs): 450
Enter target profit percentage: 20



6. Sample Output

MANUFACTURING COST AND PROFITABILITY ANALYSIS

----- MANUFACTURING COST STATEMENT -----
Material Cost       : Rs. 10000.00
Wastage Cost        : Rs. 500.00
Labour Cost         : Rs. 15000.00
Machine Cost        : Rs. 10000.00
Total Cost          : Rs. 35500.00
Total Revenue       : Rs. 45000.00
Total Profit        : Rs. 9500.00
Profit Percentage   : 26.76%
Target Profit       : 20.00%

----- PROFITABILITY RESULT -----
Production meets the specified profit target.






8. Formula Summary
Calculation	Formula
Material Cost	Production Qty × Material Qty × Material Rate
Wastage Cost	Material Cost × Wastage % / 100
Labour Cost	Production Qty × Labour Hours × Labour Rate
Machine Cost	Production Qty × Machine Hours × Machine Rate
Total Cost	Material + Wastage + Labour + Machine
Revenue	Production Qty × Selling Price
Profit	Revenue − Total Cost
Profit %	(Profit / Total Cost) × 100

Result: The sample production achieves a profit percentage of 26.76%, which exceeds the specified target of 20%. Therefore, production is considered profitable and meets the target.
