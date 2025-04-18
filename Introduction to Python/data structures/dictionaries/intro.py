# dictionaries store key value pairs

customer = {
    "name":"John Smith",
    "age": 30,
    "is_verified":True
}

print(customer["name"])

# another way of fetching value by key in a dictionary
print(customer.get("age"))