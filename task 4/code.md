1. Problem Statement
Develop a Python program to calculate an employee's monthly salary based on basic pay, allowances, overtime, and incentives.

The program should:
- Accept employee details and salary components as input.
- Calculate gross salary by adding basic pay, allowances, overtime pay, and incentives.
- Apply progressive deductions based on predefined salary slabs.
- Calculate the total deductions and net salary.
- Generate a formatted salary statement showing all salary components, deductions, and final net salary.
Objectives
- To understand arithmetic operations in Python.
- To implement conditional statements for progressive deductions.
- To calculate gross salary and net salary.
- To generate a formatted payroll statement.
2. Algorithm
1. Start.
2. Read employee ID and employee name.
3. Input basic pay, allowances, overtime hours, overtime rate, and incentives.
4. Calculate overtime pay.
Overtime Pay = Overtime Hours × Overtime Rate

5. Calculate gross salary.

Gross Salary = Basic Pay + Allowances + Overtime Pay + Incentives
6. Calculate progressive deductions:
   - First ₹10,000: 5%
   - Next ₹10,000: 10%
   - Remaining amount: 15%
7. Calculate total deductions.
8. Calculate net salary.
Net Salary = Gross Salary − Total Deductions
9. Display the formatted salary statement.
10. Stop.
3. Flowchart
~~~mermaid

flowchart TD
    A([Start]) --> B[/Input Employee ID and Name/]
    B --> C[/Input Basic Pay, Allowances,
    Overtime Hours, Overtime Rate,
    and Incentives/]
    C --> D[Calculate Overtime Pay]
    D --> E[Calculate Gross Salary]
    E --> F{Gross Salary <= 10000?}

    F -- Yes --> G[Deduction = Gross Salary * 5%]
    F -- No --> H{Gross Salary <= 20000?}

    H -- Yes --> I[Deduction = 500 +
    Remaining Amount * 10%]
    H -- No --> J[Deduction = 500 + 1000 +
    Remaining Amount * 15%]

    G --> K[Calculate Net Salary]
    I --> K
    J --> K

    K --> L[Generate Salary Statement]
    L --> M[/Display Gross Salary,
    Total Deductions, Net Salary/]
    M --> N([Stop])

~~~




5. Sample Input
Enter Employee ID: E101
Enter Employee Name: Ravi
Enter Basic Pay: 25000
Enter Allowances: 5000
Enter Overtime Hours: 10
Enter Overtime Rate per Hour: 200
Enter Incentives: 3000


6. Sample Output

======================================
         EMPLOYEE SALARY STATEMENT
======================================
Employee ID       : E101
Employee Name     : Ravi
--------------------------------------
Basic Pay         : Rs. 25000.00
Allowances        : Rs. 5000.00
Overtime Pay      : Rs. 2000.00
Incentives        : Rs. 3000.00
--------------------------------------
Gross Salary      : Rs. 35000.00
Total Deductions  : Rs. 3750.00
--------------------------------------
Net Salary        : Rs. 31250.00
======================================



Calculation
Gross Salary
\[
25000+5000+2000+3000=35000
\]

Progressive Deduction
Salary Slab	Deduction
First ₹10,000 at 5%	₹500
Next ₹10,000 at 10%	₹1,000
Remaining ₹15,000 at 15%	₹2,250
Total Deduction	₹3,750

Net Salary
\[
35000-3750=\boxed{₹31,250}
\]





8. Result
The Employee Payroll and Deduction Analysis program was successfully implemented using Python. It calculates gross salary, applies progressive deductions according to salary slabs, and generates a formatted salary statement displaying the employee's net salary.

Note: The deduction percentages used in this program are hypothetical academic rules, not actual statutory payroll tax rates.
