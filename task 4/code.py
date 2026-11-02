# Employee Payroll and Deduction Analysis

# Input employee details
emp_id = input("Enter Employee ID: ")
emp_name = input("Enter Employee Name: ")

# Input salary components
basic_pay = float(input("Enter Basic Pay: "))
allowances = float(input("Enter Allowances: "))
overtime_hours = float(input("Enter Overtime Hours: "))
overtime_rate = float(input("Enter Overtime Rate per Hour: "))
incentives = float(input("Enter Incentives: "))

# Calculate overtime pay
overtime_pay = overtime_hours * overtime_rate

# Calculate gross salary
gross_salary = basic_pay + allowances + overtime_pay + incentives

# Calculate progressive deductions
if gross_salary <= 10000:
    deduction = gross_salary * 0.05

elif gross_salary <= 20000:
    deduction = (10000 * 0.05) + ((gross_salary - 10000) * 0.10)

else:
    deduction = (10000 * 0.05) + (10000 * 0.10) + \
                ((gross_salary - 20000) * 0.15)

# Calculate net salary
net_salary = gross_salary - deduction

# Display salary statement
print("\n======================================")
print("         EMPLOYEE SALARY STATEMENT")
print("======================================")
print("Employee ID       :", emp_id)
print("Employee Name     :", emp_name)
print("--------------------------------------")
print("Basic Pay         : Rs.", format(basic_pay, ".2f"))
print("Allowances        : Rs.", format(allowances, ".2f"))
print("Overtime Pay      : Rs.", format(overtime_pay, ".2f"))
print("Incentives        : Rs.", format(incentives, ".2f"))
print("--------------------------------------")
print("Gross Salary      : Rs.", format(gross_salary, ".2f"))
print("Total Deductions  : Rs.", format(deduction, ".2f"))
print("--------------------------------------")
print("Net Salary        : Rs.", format(net_salary, ".2f"))
print("======================================")

