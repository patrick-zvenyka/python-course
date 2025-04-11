# string slicing techniques

# 1. slicing (start:stop)
company = 'Google'
print(company[0:2])  # Output: Go
print(company[1:4])  # Output: oog

# 2. slicing with step (start:stop:step)
language = 'Python'
print(language[0:5:2])  # Output: Pto
print(language[::3])     # Output: Ph

# omitting start or end
msg = 'Hello World'
print(msg[:5])   # Output: Hello
print(msg[6:])   # Output: World
print(msg[:])    # Output: Hello World (full string)
