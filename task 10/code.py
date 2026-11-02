import math

# Campus Event Financial Planning

# Input details
participants = int(input("Enter number of participants: "))

venue_cost = float(input("Enter venue cost: "))
equipment_cost = float(input("Enter equipment cost: "))

catering_per_person = float(
    input("Enter catering cost per participant: ")
)

transport_per_person = float(
    input("Enter transport cost per participant: ")
)

certificate_per_person = float(
    input("Enter certificate cost per participant: ")
)

contribution_per_person = float(
    input("Enter participant contribution per person: ")
)

sponsorship = float(input("Enter available sponsorship: "))

# Fixed cost calculation
fixed_cost = venue_cost + equipment_cost

# Variable cost per participant
variable_cost = (
    catering_per_person
    + transport_per_person
    + certificate_per_person
)

# Total variable cost
total_variable_cost = participants * variable_cost

# Total event cost
total_event_cost = fixed_cost + total_variable_cost

# Participant revenue
participant_revenue = (
    participants * contribution_per_person
)

# Total available funds
total_funds = participant_revenue + sponsorship

# Sponsorship shortfall
sponsorship_shortfall = max(
    0, total_event_cost - total_funds
)

# Surplus amount
surplus = max(0, total_funds - total_event_cost)

# Minimum registrations required to break even
net_contribution = contribution_per_person - variable_cost

if fixed_cost <= sponsorship:
    minimum_registrations = 0

elif net_contribution > 0:
    minimum_registrations = math.ceil(
        (fixed_cost - sponsorship) / net_contribution
    )

else:
    minimum_registrations = -1

# Output report
print("\n===== CAMPUS EVENT FINANCIAL REPORT =====")

print(f"Fixed Cost             : Rs. {fixed_cost:.2f}")
print(f"Variable Cost/Person   : Rs. {variable_cost:.2f}")
print(f"Total Variable Cost    : Rs. {total_variable_cost:.2f}")
print(f"Total Event Cost       : Rs. {total_event_cost:.2f}")
print(f"Participant Revenue    : Rs. {participant_revenue:.2f}")
print(f"Available Sponsorship  : Rs. {sponsorship:.2f}")

print(f"Sponsorship Shortfall  : Rs. {sponsorship_shortfall:.2f}")
print(f"Financial Surplus      : Rs. {surplus:.2f}")

if minimum_registrations == -1:
    print("Break-even is not possible with the "
          "current contribution amount.")
else:
    print(f"Minimum Registrations  : {minimum_registrations}")

if sponsorship_shortfall == 0:
    print("Status                 : Event is financially covered")
else:
    print("Status                 : Additional funds are required")

