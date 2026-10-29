products = [
    ("Notebook", 100, 4, "food"),
    ("Headphones", 500, 2, "electronics"),
]

subtotal = 0
tax_total = 0

print("RETAIL INVOICE")
print("-" * 58)
print("{:<18} {:>8} {:>8} {:>10} {:>10}".format(
    "Product", "Price", "Qty", "Tax", "Line total"
))

for product in products:
    name, price, quantity, category = product
    line_amount = price * quantity
    if category == "food":
        tax_rate = 0.05
    else:
        tax_rate = 0.18
    tax = line_amount * tax_rate
    subtotal = subtotal + line_amount
    tax_total = tax_total + tax
    print("{:<18} {:>8.2f} {:>8} {:>10.2f} {:>10.2f}".format(
        name, price, quantity, tax, line_amount + tax
    ))

if subtotal >= 1000:
    discount = subtotal * 0.10
    if discount > 150:
        discount = 150
else:
    discount = 0

final_total = subtotal + tax_total - discount

print("-" * 58)
print("Merchandise subtotal: Rs. {:.2f}".format(subtotal))
print("Tax:                 Rs. {:.2f}".format(tax_total))
print("Discount:            Rs. {:.2f}".format(discount))
print("Amount to pay:       Rs. {:.2f}".format(final_total))
