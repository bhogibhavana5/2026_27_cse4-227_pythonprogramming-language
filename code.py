# Progressive Electricity Billing System

def calculate_bill(units):

    # Progressive slab calculation
    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = (100 * 2) + ((units - 100) * 3)

    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    else:
        energy_charge = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

    # Fixed charges
    fixed_charge = 50

    # Surcharge (5%)
    surcharge = energy_charge * 0.05

    # Rebate (10% if units below 100)
    if units < 100:
        rebate = energy_charge * 0.10
    else:
        rebate = 0

    # Final bill
    total_bill = energy_charge + fixed_charge + surcharge - rebate

    return energy_charge, surcharge, rebate, total_bill


# Main program
print("===================================")
print(" PROGRESSIVE ELECTRICITY BILLING")
print("===================================")

name = input("Enter consumer name: ")

n = int(input("Enter number of months: "))

months = []
bills = []
consumptions = []

for i in range(n):

    print("\nMonth", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity units: "))

    energy, surcharge, rebate, total = calculate_bill(units)

    months.append(month)
    consumptions.append(units)
    bills.append(total)

    print("Energy Charge: Rs.", round(energy, 2))
    print("Fixed Charge: Rs. 50")
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total Bill: Rs.", round(total, 2))


# Monthly bill comparison
print("\n========== BILL COMPARISON ==========")
print("Consumer:", name)

for i in range(n):

    print(months[i], "- Units:", consumptions[i],
          "Bill: Rs.", round(bills[i], 2))

    if i > 0:

        increase = consumptions[i] - consumptions[i - 1]

        percentage = (increase / consumptions[i - 1]) * 100 if consumptions[i - 1] > 0 else 0

        if percentage > 30:
            print("WARNING: Unusual increase detected!")
            print("Consumption increased by",
                  round(percentage, 2), "%")

        else:
            print("Normal consumption change.")

print("\nElectricity billing completed!")

