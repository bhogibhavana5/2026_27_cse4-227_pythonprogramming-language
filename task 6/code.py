# Railway Fare and Reservation Calculator

# Fare rates per km for distance slabs
# Distance: 0-100 km, 101-300 km, above 300 km

fare_rates = {
    "Sleeper": [1.20, 1.00, 0.80],
    "AC3": [2.00, 1.70, 1.50],
    "AC2": [3.00, 2.50, 2.20]
}

# Reservation charges
reservation_fees = {
    "Sleeper": 20,
    "AC3": 40,
    "AC2": 50
}

# Age concession percentages
CHILD_CONCESSION = 50  # Age 5 to 12
SENIOR_CONCESSION = 40  # Age 60 and above

# Cancellation penalty percentage
CANCELLATION_RATE = 25


def calculate_basic_fare(distance, travel_class):
    rates = fare_rates[travel_class]
    fare = 0

    # First 100 km
    slab1 = min(distance, 100)
    fare += slab1 * rates[0]

    # Next 200 km (101 to 300)
    if distance > 100:
        slab2 = min(distance - 100, 200)
        fare += slab2 * rates[1]

    # Above 300 km
    if distance > 300:
        slab3 = distance - 300
        fare += slab3 * rates[2]

    return fare


def calculate_concession(age):
    if 5 <= age <= 12:
        return CHILD_CONCESSION
    elif age >= 60:
        return SENIOR_CONCESSION
    else:
        return 0


def main():
    total_payable = 0

    print("RAILWAY FARE AND RESERVATION CALCULATOR")
    print("---------------------------------------")

    while True:
        try:
            n = int(input("Enter number of passengers: "))
            if n > 0:
                break
            print("Passenger count must be positive.")
        except ValueError:
            print("Enter a valid integer.")

    for i in range(1, n + 1):
        print(f"\nPassenger {i}")

        name = input("Enter passenger name: ")

        while True:
            try:
                age = int(input("Enter age: "))
                if age >= 0:
                    break
                print("Age cannot be negative.")
            except ValueError:
                print("Enter a valid age.")

        while True:
            try:
                distance = float(input("Enter travel distance (km): "))
                if distance > 0:
                    break
                print("Distance must be positive.")
            except ValueError:
                print("Enter a valid distance.")

        while True:
            travel_class = input(
                "Enter class (Sleeper/AC3/AC2): "
            ).strip()

            if travel_class in fare_rates:
                break
            print("Invalid class. Choose Sleeper, AC3, or AC2.")

        # Calculate basic fare
        basic_fare = calculate_basic_fare(
            distance, travel_class
        )

        # Calculate age concession
        concession_percent = calculate_concession(age)
        concession_amount = (
            basic_fare * concession_percent / 100
        )

        discounted_fare = basic_fare - concession_amount

        # Add reservation fee
        reservation_fee = reservation_fees[travel_class]

        total_fare = discounted_fare + reservation_fee

        # Cancellation details
        cancelled = input(
            "Is the ticket cancelled? (yes/no): "
        ).strip().lower()

        if cancelled == "yes":
            penalty = (
                discounted_fare * CANCELLATION_RATE / 100
                + reservation_fee
            )

            refund = total_fare - penalty
            payable = penalty

            status = "Cancelled"
        else:
            penalty = 0
            refund = 0
            payable = total_fare

            status = "Confirmed"

        total_payable += payable

        # Display passenger statement
        print("\n----- FARE STATEMENT -----")
        print("Passenger Name      :", name)
        print("Age                 :", age)
        print("Distance            :", distance, "km")
        print("Travel Class        :", travel_class)
        print("Basic Fare          : Rs.", round(basic_fare, 2))
        print("Concession (%)      :", concession_percent)
        print("Concession Amount   : Rs.",
              round(concession_amount, 2))
        print("Discounted Fare     : Rs.",
              round(discounted_fare, 2))
        print("Reservation Fee     : Rs.",
              round(reservation_fee, 2))
        print("Total Ticket Fare   : Rs.",
              round(total_fare, 2))
        print("Ticket Status       :", status)

        if cancelled == "yes":
            print("Cancellation Penalty: Rs.",
                  round(penalty, 2))
            print("Refund Amount       : Rs.",
                  round(refund, 2))

        print("Amount Payable      : Rs.",
              round(payable, 2))

    print("\n================================")
    print("TOTAL AMOUNT PAYABLE: Rs.",
          round(total_payable, 2))
    print("================================")


if __name__ == "__main__":
    main()

