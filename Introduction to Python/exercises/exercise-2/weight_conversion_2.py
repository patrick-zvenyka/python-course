weight = float(input("Your weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == 'L':
    print(f"Your weight is {round(weight * 0.45, 2)} kilograms")
else:
    print(f"Your weight is {round(weight / 0.45, 2)} pounds")
