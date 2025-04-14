price = 1000000

buyer = input("Good credit or bad credit?: ")

if buyer.lower() == 'good':
    payment = 0.1 * price
else:
    payment = 0.2 * price
print(f"Buyer must pay ${payment}")
