
# Retail Billing with Multiple Discount Rules

# Category-specific tax rates
TAX_RATES = {
    "electronics": 18,
    "clothing": 5,
    "grocery": 3
}

# Discount rules
MAX_CONCESSION = 2000


def calculate_discount(subtotal):
    discount = 0

    if subtotal >= 5000:
        discount += subtotal * 0.05

    if subtotal >= 10000:
        discount += subtotal * 0.10

    # Apply maximum concession limit
    discount = min(discount, MAX_CONCESSION)

    return discount


# Input number of products
n = int(input("Enter number of products: "))

products = []
subtotal = 0

# Read product details
for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (electronics/clothing/grocery): ").lower()
    price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))

    if category not in TAX_RATES:
        print("Invalid category! Please enter a valid category.")
        exit()

    if price < 0 or quantity <= 0:
        print("Invalid price or quantity!")
        exit()

    item_subtotal = price * quantity

    products.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "subtotal": item_subtotal
    })

    subtotal += item_subtotal

# Calculate discount
discount = calculate_discount(subtotal)

# Calculate invoice details
total_tax = 0
taxable_total = 0

print("\n" + "=" * 75)
print("                    RETAIL INVOICE")
print("=" * 75)

print(f"{'Product':<15}{'Qty':<6}{'Price':<10}"
      f"{'Subtotal':<12}{'Discount':<12}{'Tax':<10}{'Total':<10}")

print("-" * 75)

for item in products:

    # Allocate discount proportionally to each item
    item_discount = (item["subtotal"] / subtotal) * discount

    taxable_amount = item["subtotal"] - item_discount

    tax_rate = TAX_RATES[item["category"]]

    tax = taxable_amount * tax_rate / 100

    item_total = taxable_amount + tax

    total_tax += tax
    taxable_total += taxable_amount

    print(f"{item['name']:<15}"
          f"{item['quantity']:<6}"
          f"{item['price']:<10.2f}"
          f"{item['subtotal']:<12.2f}"
          f"{item_discount:<12.2f}"
          f"{tax:<10.2f}"
          f"{item_total:<10.2f}")

# Final bill
final_amount = taxable_total + total_tax

print("-" * 75)
print(f"Subtotal             : Rs. {subtotal:.2f}")
print(f"Total Discount       : Rs. {discount:.2f}")
print(f"Taxable Amount       : Rs. {taxable_total:.2f}")
print(f"Total Tax            : Rs. {total_tax:.2f}")
print("=" * 75)
print(f"FINAL PAYABLE AMOUNT : Rs. {final_amount:.2f}")
print("=" * 75)
print("            Thank you for shopping!")
