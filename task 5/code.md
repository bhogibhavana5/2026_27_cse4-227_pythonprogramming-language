1. Problem Statement
To develop a Python program that evaluates multiple mobile telecommunications plans based on the user's data usage, call minutes, SMS usage, plan validity, and budget constraints.

The program calculates the total cost of each plan, including excess usage charges. It identifies the eligible plan with the lowest total cost while satisfying the user's budget and validity requirements.

The system displays the plan details, excess charges, total cost, and the most economical eligible plan.
2. Algorithm
1. Start.
2. Input the user's:
   - Data usage in GB.
   - Call usage in minutes.
   - SMS usage count.
   - Required validity in days.
   - Maximum budget.
3. Input the number of mobile plans.
4. For each plan, input:
   - Plan name.
   - Base price.
   - Included data in GB.
   - Included call minutes.
   - Included SMS count.
   - Validity in days.
   - Excess data charge per GB.
   - Excess call charge per minute.
   - Excess SMS charge per message.
5. Check whether the plan satisfies the validity requirement.
6. Calculate excess data, call, and SMS usage.
7. Calculate the excess charges.
8. Calculate the total plan cost.
9. Check whether the total cost is within the user's budget.
10. Store all eligible plans.
11. Find the eligible plan with the minimum total cost.
12. Display all plan costs and the best eligible plan.
13. If no plan is eligible, display a suitable message.
14. Stop.
3. Flowchart
~~~mermaid

flowchart TD
    A([Start]) --> B[/Read data, calls, SMS, validity and budget/]
    B --> C[/Read number of plans N/]
    C --> D[Set i = 1]
    D --> E[/Read plan details/]
    E --> F[Calculate excess data]
    F --> G[Calculate excess calls]
    G --> H[Calculate excess SMS]
    H --> I[Calculate total cost]
    I --> J{Validity >= Required validity?}
    J -- No --> K[Mark as ineligible]
    J -- Yes --> L{Total cost <= Budget?}
    L -- No --> K
    L -- Yes --> M[Add plan to eligible list]
    K --> N{i < N?}
    M --> N
    N -- Yes --> O[i = i + 1]
    O --> E
    N -- No --> P{Eligible list empty?}
    P -- Yes --> Q[/Display no eligible plan/]
    P -- No --> R[Find plan with minimum total cost]
    R --> S[/Display best plan and savings/]
    Q --> T([Stop])
    S --> T


~~~



5. Sample Input

Enter data usage (GB): 2.5
Enter call usage (minutes): 350
Enter SMS usage: 80
Enter required validity (days): 28
Enter maximum budget (Rs): 300
Enter number of mobile plans: 3

Enter details for Plan 1
Plan name: Basic
Base price (Rs): 199
Included data (GB): 1.5
Included call minutes: 300
Included SMS: 100
Validity (days): 28
Excess data charge per GB (Rs): 50
Excess call charge per minute (Rs): 0.5
Excess SMS charge per message (Rs): 0.1

Enter details for Plan 2
Plan name: Smart
Base price (Rs): 249
Included data (GB): 3
Included call minutes: 500
Included SMS: 100
Validity (days): 28
Excess data charge per GB (Rs): 40
Excess call charge per minute (Rs): 0.5
Excess SMS charge per message (Rs): 0.1

Enter details for Plan 3
Plan name: Ultra
Base price (Rs): 299
Included data (GB): 5
Included call minutes: 1000
Included SMS: 200
Validity (days): 56
Excess data charge per GB (Rs): 30
Excess call charge per minute (Rs): 0.5
Excess SMS charge per message (Rs): 0.1



6. Sample Output

========== PLAN COMPARISON ==========

Plan Name: Basic
Base Price: Rs. 199.0
Excess Data Charge: Rs. 50.0
Excess Call Charge: Rs. 25.0
Excess SMS Charge: Rs. 0.0
Total Cost: Rs. 274.0
Status: Eligible

Plan Name: Smart
Base Price: Rs. 249.0
Excess Data Charge: Rs. 0.0
Excess Call Charge: Rs. 0.0
Excess SMS Charge: Rs. 0.0
Total Cost: Rs. 249.0
Status: Eligible

Plan Name: Ultra
Base Price: Rs. 299.0
Excess Data Charge: Rs. 0.0
Excess Call Charge: Rs. 0.0
Excess SMS Charge: Rs. 0.0
Total Cost: Rs. 299.0
Status: Not Eligible

========== RESULT ==========

Most Economical Plan: Smart
Total Cost: Rs. 249.0
Validity: 28 days
Remaining Budget: Rs. 51.0





8. Result
The program compares three telecommunications plans based on data usage, call usage, SMS usage, validity, and budget.
- Basic Plan: ₹274
- Smart Plan: ₹249
- Ultra Plan: ₹299 (exceeds the budget)
Best Plan: Smart — ₹249
The Smart plan is the most economical eligible plan because it satisfies the required validity of 28 days and stays within the maximum budget of ₹300.












Do you like this personality?
