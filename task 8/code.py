# Manufacturing Cost and Profitability Analysis

print("MANUFACTURING COST AND PROFITABILITY ANALYSIS")

# Input details
production_qty = int(input("Enter number of units produced: "))

material_qty = float(input("Enter material quantity per unit (kg): "))
material_rate = float(input("Enter material cost per kg (Rs): "))

labour_hours = float(input("Enter labour hours per unit: "))
labour_rate = float(input("Enter labour rate per hour (Rs): "))

wastage_percent = float(input("Enter wastage percentage: "))

machine_hours = float(input("Enter machine hours per unit: "))
machine_rate = float(input("Enter machine rate per hour (Rs): "))

selling_price = float(input("Enter selling price per unit (Rs): "))
profit_target = float(input("Enter target profit percentage: "))

# Cost calculations
material_cost = production_qty * material_qty * material_rate

wastage_cost = material_cost * wastage_percent / 100

labour_cost = production_qty * labour_hours * labour_rate

machine_cost = production_qty * machine_hours * machine_rate

total_cost = material_cost + wastage_cost + labour_cost + machine_cost

# Revenue calculation
total_revenue = production_qty * selling_price

# Profit or loss calculation
profit = total_revenue - total_cost

# Profit percentage
if total_cost > 0:
    profit_percent = (profit / total_cost) * 100
else:
    profit_percent = 0

# Display cost statement
print("\n----- MANUFACTURING COST STATEMENT -----")
print(f"Material Cost       : Rs. {material_cost:.2f}")
print(f"Wastage Cost        : Rs. {wastage_cost:.2f}")
print(f"Labour Cost         : Rs. {labour_cost:.2f}")
print(f"Machine Cost        : Rs. {machine_cost:.2f}")
print(f"Total Cost          : Rs. {total_cost:.2f}")
print(f"Total Revenue       : Rs. {total_revenue:.2f}")

if profit >= 0:
    print(f"Total Profit        : Rs. {profit:.2f}")
else:
    print(f"Total Loss          : Rs. {abs(profit):.2f}")

print(f"Profit Percentage   : {profit_percent:.2f}%")
print(f"Target Profit       : {profit_target:.2f}%")

# Profitability analysis
print("\n----- PROFITABILITY RESULT -----")

if profit_percent >= profit_target:
    print("Production meets the specified profit target.")
else:
    print("Production does not meet the specified profit target.")

