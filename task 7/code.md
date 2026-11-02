Retail Billing with Multiple Discount Rules
1. Problem Statement
Develop a Python program to generate an itemized retail invoice for multiple products purchased by a customer.

The system should:
- Accept multiple products and their quantities.
- Calculate the subtotal for each product.
- Apply category-specific taxes.
- Apply threshold-based discounts when the purchase amount exceeds specified limits.
- Enforce a maximum concession limit.
- Calculate the final payable amount.
- Generate a formatted itemized invoice.
Discount and Tax Rules
Rule	Condition
Electronics Tax	18%
Clothing Tax	5%
Grocery Tax	3%
Discount 1	5% if subtotal ≥ ₹5,000
Discount 2	Additional 10% if subtotal ≥ ₹10,000
Maximum concession	₹2,000
Tax calculation	Tax is calculated after discount

These are sample rules for the program and can be modified as needed.
2. Algorithm
1. Start the program.
2. Read the number of products.
3. For each product:
   - Read product name.
   - Read category.
   - Read unit price.
   - Read quantity.
   - Calculate item subtotal.
   - Determine the category-specific tax rate.
   - Add the item subtotal to the total subtotal.
4. Check the discount thresholds.
5. Calculate the total discount.
6. Apply the maximum concession limit.
7. Calculate the taxable amount.
8. Calculate the total tax.
9. Calculate the final bill amount.
10. Display the itemized invoice.
11. Stop.
3. Flowchart
  ~~~mermaid

flowchart TD
    A([Start]) --> B[/Input number of products/]
    B --> C[Initialize subtotal = 0]
    C --> D[/Input product name, category, price, quantity/]
    D --> E{Valid category?}
    E -- No --> F[Display error]
    F --> Z([Stop])
    E -- Yes --> G[Calculate item subtotal]
    G --> H[Add item subtotal to total subtotal]
    H --> I{More products?}
    I -- Yes --> D
    I -- No --> J{Subtotal >= 5000?}
    J -- Yes --> K[Apply 5 percent discount]
    J -- No --> L[Discount remains 0]
    K --> M{Subtotal >= 10000?}
    L --> M
    M -- Yes --> N[Add 10 percent discount]
    M -- No --> O[Keep current discount]
    N --> P[Limit discount to maximum 2000]
    O --> P
    P --> Q[Allocate discount proportionally]
    Q --> R[Calculate taxable amount]
    R --> S[Calculate category-specific tax]
    S --> T[Calculate final payable amount]
    T --> U[/Print itemized invoice/]
    U --> V([Stop])

~~~






5. Sample Input
Enter number of products: 3

Product 1
Enter product name: Laptop
Enter category (electronics/clothing/grocery): electronics
Enter unit price: 40000
Enter quantity: 1

Product 2
Enter product name: Shirt
Enter category (electronics/clothing/grocery): clothing
Enter unit price: 2000
Enter quantity: 2

Product 3
Enter product name: Rice
Enter category (electronics/clothing/grocery): grocery
Enter unit price: 1000
Enter quantity: 3


6. Sample Output

===========================================================================
                         RETAIL INVOICE
===========================================================================
Product        Qty   Price     Subtotal    Discount    Tax       Total
---------------------------------------------------------------------------
Laptop         1     40000.00  40000.00    1702.13     6893.62   45191.49
Shirt          2     2000.00   4000.00     170.21      191.49    4000.00
Rice           3     1000.00   3000.00     127.66      86.17     2958.51
---------------------------------------------------------------------------
Subtotal             : Rs. 47000.00
Total Discount       : Rs. 2000.00
Taxable Amount       : Rs. 45000.00
Total Tax            : Rs. 7171.28
===========================================================================
FINAL PAYABLE AMOUNT : Rs. 52171.28
===========================================================================
            Thank you for shopping!






Note: The code uses cumulative discount rules: 5% and an additional 10% for bills of ₹10,000 or more, subject to the ₹2,000 maximum concession. Taxes are calculated after the discount.






