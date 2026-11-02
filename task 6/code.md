Railway Fare and Reservation Calculator – Python Program
1. Problem Statement
The Railway Fare and Reservation Calculator is a Python program designed to calculate the total railway fare for multiple passengers based on distance traveled, travel class, age-based concessions, reservation fees, and cancellation penalties.

The program performs the following operations:
- Accepts passenger details such as name, age, travel distance, and travel class.
- Calculates the basic fare using predefined distance slabs.
- Applies different fare rates for travel classes such as Sleeper, AC 3-Tier, and AC 2-Tier.
- Provides age-based concessions for children and senior citizens.
- Adds reservation charges to the ticket fare.
- Calculates cancellation penalties when a ticket is cancelled.
- Displays a detailed fare statement for each passenger.
- Calculates the total amount payable for all passengers.
2. Algorithm
1. Start the program.
2. Define distance slabs and fare rates for each travel class.
3. Define age-based concession percentages.
4. Define reservation charges and cancellation penalty rates.
5. Read the number of passengers.
6. For each passenger:
   - Read passenger name, age, distance, and travel class.
   - Validate the input details.
   - Calculate the basic fare using the distance slab and travel class.
   - Apply the age-based concession.
   - Calculate the reservation fee.
   - Calculate the final ticket fare.
   - Ask whether the ticket is cancelled.
   - If cancelled, calculate the cancellation penalty and refund.
   - Otherwise, consider the final fare as payable.
7. Display the fare details for each passenger.
8. Calculate and display the total amount payable.
9. Stop the program.
3. Flowchart

~~~mermaid

flowchart TD
    A([Start]) --> B[/Enter number of passengers/]
    B --> C[Initialize total payable = 0]
    C --> D[/Enter passenger name, age, distance and class/]
    D --> E{Is input valid?}
    E -- No --> D
    E -- Yes --> F[Calculate basic fare using distance slabs]
    F --> G[Calculate age concession]
    G --> H[Calculate discounted fare]
    H --> I[Add reservation fee]
    I --> J[Calculate total ticket fare]
    J --> K{Is ticket cancelled?}

    K -- Yes --> L[Calculate cancellation penalty]
    L --> M[Calculate refund amount]
    M --> N[Amount payable = penalty]

    K -- No --> O[Amount payable = total ticket fare]

    N --> P[Display passenger fare statement]
    O --> P

    P --> Q[Add amount payable to total]
    Q --> R{More passengers?}

    R -- Yes --> D
    R -- No --> S[Display total amount payable]
    S --> T([Stop])

~~~



5. Sample Input
Enter number of passengers: 3

Passenger 1
Enter passenger name: Ravi
Enter age: 30
Enter travel distance (km): 250
Enter class (Sleeper/AC3/AC2): Sleeper
Is the ticket cancelled? (yes/no): yes

Passenger 2
Enter passenger name: Sita
Enter age: 65
Enter travel distance (km): 500
Enter class (Sleeper/AC3/AC2): AC3
Is the ticket cancelled? (yes/no): no

Passenger 3
Enter passenger name: Arun
Enter age: 10
Enter travel distance (km): 120
Enter class (Sleeper/AC3/AC2): Sleeper
Is the ticket cancelled? (yes/no): no


6. Sample Output

RAILWAY FARE AND RESERVATION CALCULATOR
---------------------------------------

----- FARE STATEMENT -----
Passenger Name      : Ravi
Age                 : 30
Distance            : 250.0 km
Travel Class        : Sleeper
Basic Fare          : Rs. 270.0
Concession (%)      : 0
Concession Amount   : Rs. 0.0
Discounted Fare     : Rs. 270.0
Reservation Fee     : Rs. 20
Total Ticket Fare   : Rs. 290.0
Ticket Status       : Cancelled
Cancellation Penalty: Rs. 87.5
Refund Amount       : Rs. 202.5
Amount Payable      : Rs. 87.5

----- FARE STATEMENT -----
Passenger Name      : Sita
Age                 : 65
Distance            : 500.0 km
Travel Class        : AC3
Basic Fare          : Rs. 840.0
Concession (%)      : 40
Concession Amount   : Rs. 336.0
Discounted Fare     : Rs. 504.0
Reservation Fee     : Rs. 40
Total Ticket Fare   : Rs. 544.0
Ticket Status       : Confirmed
Amount Payable      : Rs. 544.0

----- FARE STATEMENT -----
Passenger Name      : Arun
Age                 : 10
Distance            : 120.0 km
Travel Class        : Sleeper
Basic Fare          : Rs. 140.0
Concession (%)      : 50
Concession Amount   : Rs. 70.0
Discounted Fare     : Rs. 70.0
Reservation Fee     : Rs. 20
Total Ticket Fare   : Rs. 90.0
Ticket Status       : Confirmed
Amount Payable      : Rs. 90.0

================================
TOTAL AMOUNT PAYABLE: Rs. 721.5
================================







Important Note
The fare rates and concession percentages in this program are assumed values for academic purposes. They do not represent the actual Indian Railways fare rules.
- Distance slabs: 0–100 km, 101–300 km, and above 300 km.
- Sleeper, AC3, and AC2 classes have different per-kilometer rates.
- Children aged 5–12 receive a 50% concession.
- Senior citizens aged 60 and above receive a 40% concession.
- Cancellation penalty is 25% of the discounted fare plus the non-refundable reservation fee.
This program demonstrates Python concepts such as functions, loops, conditional statements, dictionaries, input validation, arithmetic calculations, and formatted output.
