import math
from datetime import datetime

DISCOUNT_RATE = 0.10
TAX_RATE = 0.06

subtotal = 0
price = 1

price = float(input("Please enter the price: "))
if price != 0:

    quantity = int(input("Please enter the quantity: "))

    subtotal = price * quantity


subtotal = round(subtotal, 2)
print()
print(f"Subtotal: ${subtotal:.2f}")

current_date_and_time = datetime.now()

weekday = current_date_and_time.weekday()

if weekday == 1 or weekday == 2:
    if subtotal < 50:
        needed_amount = 50 - subtotal
        print("To receive your discount, add {lacking:.2f} to your order.")
    else:
        discount = round(subtotal * DISCOUNT_RATE, 2)
        print(f"Total discount: {discount:.2f}")
        subtotal -= discount

tax = round(subtotal * TAX_RATE, 2)
print(f"Total sales tax: ${tax:.2f}")

grand_total = subtotal + tax

print(f"Your grandtotal is: ${grand_total:.2f}""\n")