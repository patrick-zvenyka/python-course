# a simple program to tell someone what
# to do for a certain weather condition

is_hot = True
is_cold = True
if is_hot:
    print("It's a hot day, drink a lot of water!")
elif is_cold:
    print("It's a cold day wear warm clothes")
else:
    print("enjoy your day!")

# the code below is the advanced version of the program above

temp = 0
x = int(input("Enter temperature: "))
temp += x

if temp >= 39:
    print("It's a hot day, drink a lot of water!")
elif temp <= 30:
    print("It's a cold day wear warm clothes!")
else:
    print("The weather is nice, enjoy your day!")
