Progressive Electricity Billing System Using Python
1. Problem Statement
Develop a Progressive Electricity Billing System using Python to calculate household electricity bills based on multiple consumption slabs.

The system should:
- Accept the consumer's name and monthly electricity consumption.
- Calculate electricity charges using progressive slab rates.
- Add fixed charges to the electricity bill.
- Apply additional surcharges.
- Provide rebates or discounts when applicable.
- Calculate the final payable amount.
- Compare electricity bills across several months.
- Identify unusual increases in electricity consumption and bill amounts.
The system helps households understand their electricity usage and manage their monthly expenses.
2. Algorithm
1. Start the program.
2. Enter the consumer's name.
3. Enter the number of months for bill comparison.
4. For each month, enter electricity consumption in units (kWh).
5. Calculate energy charges using progressive slabs:
   - 0–100 units: ₹2 per unit
   - 101–200 units: ₹3 per unit
   - 201–300 units: ₹5 per unit
   - Above 300 units: ₹7 per unit
6. Add fixed charges of ₹50.
7. Calculate a surcharge of 5% on energy charges.
8. Apply a 10% rebate on energy charges if consumption is below 100 units.
9. Calculate the final bill amount.
10. Store the monthly bill details.
11. Compare each month's consumption with the previous month.
12. If consumption increases by more than 30%, identify it as an unusual increase.
13. Display all monthly bills and unusual increases.
14. Stop the program.
3. Flowchart
   ~~~mermaid
   
flowchart TD
    A([Start]) --> B[/Enter Consumer Name/]
    B --> C[/Enter Number of Months/]
    C --> D[/Enter Month and Units/]

    D --> E{Units <= 100?}

    E -- Yes --> F[Calculate at Rs.2 per unit]
    E -- No --> G{Units <= 200?}

    G -- Yes --> H[Calculate first 100 at Rs.2<br/>Remaining at Rs.3]
    G -- No --> I{Units <= 300?}

    I -- Yes --> J[Calculate slabs at Rs.2, Rs.3 and Rs.5]
    I -- No --> K[Calculate slabs at Rs.2, Rs.3, Rs.5 and Rs.7]

    F --> L[Add Fixed Charge]
    H --> L
    J --> L
    K --> L

    L --> M[Calculate 5% Surcharge]
    M --> N{Units < 100?}

    N -- Yes --> O[Apply 10% Rebate]
    N -- No --> P[No Rebate]

    O --> Q[Calculate Final Bill]
    P --> Q

    Q --> R{More Months?}
    R -- Yes --> D
    R -- No --> S[Display Monthly Bills]

    S --> T[Compare Monthly Consumption]
    T --> U{Increase > 30%?}

    U -- Yes --> V[Display Unusual Increase Warning]
    U -- No --> W[Display Normal Consumption]

    V --> X([End])
    W --> X

   ~~~



studocu.com



5. Sample Input
Enter consumer name: Bhavana
Enter number of months: 3

Month 1
Enter month name: January
Enter electricity units: 80

Month 2
Enter month name: February
Enter electricity units: 150

Month 3
Enter month name: March
Enter electricity units: 250


6. Sample Output
===================================
 PROGRESSIVE ELECTRICITY BILLING
===================================

Month 1
Energy Charge: Rs. 160.00
Fixed Charge: Rs. 50
Surcharge: Rs. 8.00
Rebate: Rs. 16.00
Total Bill: Rs. 202.00

Month 2
Energy Charge: Rs. 350.00
Fixed Charge: Rs. 50
Surcharge: Rs. 17.50
Rebate: Rs. 0
Total Bill: Rs. 417.50

Month 3
Energy Charge: Rs. 850.00
Fixed Charge: Rs. 50
Surcharge: Rs. 42.50
Rebate: Rs. 0
Total Bill: Rs. 942.50

========== BILL COMPARISON ==========

Consumer: Bhavana

January - Units: 80.0 Bill: Rs. 202.0

February - Units: 150.0 Bill: Rs. 417.5
WARNING: Unusual increase detected!
Consumption increased by 87.5 %

March - Units: 250.0 Bill: Rs. 942.5
WARNING: Unusual increase detected!
Consumption increased by 66.67 %

Electricity billing completed!



8. Expected Result
The Progressive Electricity Billing System successfully:
1. Calculates electricity charges using multiple consumption slabs.
2. Adds fixed charges and surcharges.
3. Applies rebates based on electricity usage.
4. Compares monthly electricity bills.
5. Detects unusual increases in electricity consumption.
Conclusion: This Python program provides an efficient way to calculate household electricity bills, compare monthly usage, and identify unusual electricity consumption patterns.

Note: The slab rates and charges used here are example values for an academic project, not official electricity tariff rates.

