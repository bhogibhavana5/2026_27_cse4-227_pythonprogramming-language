# Multi-Plan Telecommunications Cost Optimization

# Input user requirements
data_usage = float(input("Enter data usage (GB): "))
call_usage = int(input("Enter call usage (minutes): "))
sms_usage = int(input("Enter SMS usage: "))
required_validity = int(input("Enter required validity (days): "))
budget = float(input("Enter maximum budget (Rs): "))

n = int(input("Enter number of mobile plans: "))

plans = []
eligible_plans = []

# Input plan details
for i in range(n):
    print("\nEnter details for Plan", i + 1)

    name = input("Plan name: ")
    base_price = float(input("Base price (Rs): "))
    included_data = float(input("Included data (GB): "))
    included_calls = int(input("Included call minutes: "))
    included_sms = int(input("Included SMS: "))
    validity = int(input("Validity (days): "))

    data_rate = float(input("Excess data charge per GB (Rs): "))
    call_rate = float(input("Excess call charge per minute (Rs): "))
    sms_rate = float(input("Excess SMS charge per message (Rs): "))

    # Calculate excess usage
    excess_data = max(0, data_usage - included_data)
    excess_calls = max(0, call_usage - included_calls)
    excess_sms = max(0, sms_usage - included_sms)

    # Calculate excess charges
    data_charge = excess_data * data_rate
    call_charge = excess_calls * call_rate
    sms_charge = excess_sms * sms_rate

    # Calculate total cost
    total_cost = base_price + data_charge + call_charge + sms_charge

    # Store plan details
    plan = {
        "name": name,
        "base_price": base_price,
        "data_charge": data_charge,
        "call_charge": call_charge,
        "sms_charge": sms_charge,
        "total_cost": total_cost,
        "validity": validity
    }

    plans.append(plan)

    # Check eligibility
    if validity >= required_validity and total_cost <= budget:
        eligible_plans.append(plan)

# Display plan comparison
print("\n========== PLAN COMPARISON ==========")

for plan in plans:
    print("\nPlan Name:", plan["name"])
    print("Base Price: Rs.", plan["base_price"])
    print("Excess Data Charge: Rs.", round(plan["data_charge"], 2))
    print("Excess Call Charge: Rs.", round(plan["call_charge"], 2))
    print("Excess SMS Charge: Rs.", round(plan["sms_charge"], 2))
    print("Total Cost: Rs.", round(plan["total_cost"], 2))

    if (plan["validity"] >= required_validity
            and plan["total_cost"] <= budget):
        print("Status: Eligible")
    else:
        print("Status: Not Eligible")

# Find most economical eligible plan
print("\n========== RESULT ==========")

if eligible_plans:
    best_plan = min(
        eligible_plans,
        key=lambda plan: plan["total_cost"]
    )

    print("Most Economical Plan:", best_plan["name"])
    print("Total Cost: Rs.", round(best_plan["total_cost"], 2))
    print("Validity:", best_plan["validity"], "days")
    print("Remaining Budget: Rs.",
          round(budget - best_plan["total_cost"], 2))
else:
    print("No eligible mobile plan found.")
    print("Please increase your budget or reduce requirements.")

