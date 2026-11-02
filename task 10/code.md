Campus Event Financial Planning – Python Program
1. Problem Statement
Develop a Python program to perform financial planning for a campus event. The program calculates the total event expenditure based on venue, equipment, catering, transport, and certificate costs.

It should also:
- Calculate the total event cost.
- Determine the participant contribution per person.
- Calculate the sponsorship amount required to cover the financial shortfall.
- Check whether the available sponsorship is sufficient.
- Calculate the minimum number of participants required to break even.
- Display a detailed financial report.
2. Algorithm
1. Start the program.
2. Read the number of participants.
3. Read venue cost, equipment cost, catering cost per participant, transport cost per participant, and certificate cost per participant.
4. Read the available sponsorship amount.
5. Calculate the fixed cost:
   - Venue cost + Equipment cost.
6. Calculate the variable cost per participant:
   - Catering + Transport + Certificate.
7. Calculate total event cost.
8. Calculate the participant contribution per person after sponsorship.
9. Calculate the sponsorship shortfall, if any.
10. Calculate the minimum registration count required to break even.
11. Display all financial details.
12. Stop.
3. Flowchart
   ~~~mermaid
   
flowchart TD
    A([Start]) --> B[/Read number of participants/]
    B --> C[/Read venue and equipment costs/]
    C --> D[/Read catering, transport, certificate costs/]
    D --> E[/Read contribution per participant and sponsorship/]

    E --> F[Fixed Cost = Venue + Equipment]
    F --> G[Variable Cost = Catering + Transport + Certificate]
    G --> H[Total Event Cost = Fixed Cost + Participants * Variable Cost]

    H --> I[Participant Revenue = Participants * Contribution]
    I --> J[Total Funds = Participant Revenue + Sponsorship]
    J --> K[Shortfall = Max of 0 and Total Event Cost - Total Funds]

    K --> L{Fixed Cost <= Sponsorship?}
    L -->|Yes| M[Minimum Registrations = 0]
    L -->|No| N{Contribution > Variable Cost?}

    N -->|Yes| O[Minimum Registrations = Ceiling of Fixed Cost - Sponsorship divided by Net Contribution]
    N -->|No| P[Break-even is not possible]

    M --> Q[/Display financial report/]
    O --> Q
    P --> Q

    Q --> R([Stop])

   ~~~



5. Sample Input

Enter number of participants: 200
Enter venue cost: 50000
Enter equipment cost: 20000
Enter catering cost per participant: 250
Enter transport cost per participant: 100
Enter certificate cost per participant: 50
Enter participant contribution per person: 600
Enter available sponsorship: 30000



6. Sample Output

===== CAMPUS EVENT FINANCIAL REPORT =====
Fixed Cost             : Rs. 70000.00
Variable Cost/Person   : Rs. 400.00
Total Variable Cost    : Rs. 80000.00
Total Event Cost       : Rs. 150000.00
Participant Revenue    : Rs. 120000.00
Available Sponsorship  : Rs. 30000.00
Sponsorship Shortfall  : Rs. 0.00
Financial Surplus      : Rs. 0.00
Minimum Registrations  : 200
Status                 : Event is financially covered




8. Important Formulae
Calculation	Formula
Fixed Cost	Venue + Equipment
Variable Cost per Person	Catering + Transport + Certificate
Total Event Cost	Fixed Cost + (Participants × Variable Cost)
Participant Revenue	Participants × Contribution per Person
Sponsorship Shortfall	Max(0, Total Cost − Participant Revenue − Sponsorship)
Net Contribution	Contribution per Person − Variable Cost

Minimum registrations required to break even:
\[
N = \left\lceil \frac{F-S}{C-V} \right\rceil
\]

Where:
- \(F\) = Fixed cost
- \(S\) = Sponsorship amount
- \(C\) = Participant contribution per person
- \(V\) = Variable cost per person
For the sample:
\[
N = \frac{70000-30000}{600-400}
\]

\[
N = \frac{40000}{200} = 200
\]




Revenue
Total cost
Loss
Profit

10203040506050010001500Quantity$Q*




\(Q^*=\frac{F}{p-v}=\frac{\text{600}}{\text{35}-\text{15}}=\text{30}\)
Q* is the break-even quantity where total revenue matches total cost.

\(F\)

$



\(v\)

$/unit



\(p\)

$/unit









Give feedback

Result: The campus event requires 200 registrations to break even, with a total expenditure of ₹1,50,000 and no sponsorship shortfall.
