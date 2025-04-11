# Use the same method from the first example to call the functions

# 1. Integer: Counting students
def count_students():
    number_of_students = 30
    print(f"Number of students: {number_of_students}")

#call the function
count_students()

# 2. Float: Product price
def product_price():
    price = 12.99
    print(f"Price of the item: ${price}")

# 3. Complex: Electrical engineering value
def electric_value():
    current = 3 + 2j
    print(f"Electric current: {current}")

# 4. String: Name of a user
def user_name():
    name = "Patrick Zvenyika"
    print(f"User Name: {name}")

# 5. Boolean: Eligibility for discount
def check_discount():
    is_eligible = True
    print(f"Eligible for discount: {is_eligible}")

# 6. List: Shopping items
def shopping_list():
    items = ["bread", "milk", "eggs"]
    print(f"Shopping List: {items}")

# 7. Tuple: Room dimensions
def room_size():
    dimensions = (10, 12, 8)
    print(f"Room Dimensions (LxWxH): {dimensions}")

# 8. Range: Print days of the week
def print_days():
    for day in range(1, 8):
        print(f"Day {day}")

# 9. Dictionary: Student profile
def student_profile():
    student = {
        "name": "Patrick",
        "age": 25,
        "program": "Computer Science"
    }
    print(f"Student Profile: {student}")

# 10. Set: Unique cities visited
def unique_cities():
    cities = {"Harare", "Gweru", "Masvingo"}
    print(f"Visited Cities: {cities}")

# 11. Frozenset: Weekdays
def show_weekdays():
    weekdays = frozenset(["Mon", "Tue", "Wed", "Thu", "Fri"])
    print(f"Weekdays: {weekdays}")

# 12. Bytes: Binary command to printer
def printer_command():
    command = b"PRINT"
    print(f"Command sent to printer: {command}")

# 13. Bytearray: Modify byte data
def modify_bytes():
    data = bytearray(b"Hello")
    data[0] = 74  # Changes 'H' to 'J'
    print(f"Modified bytearray: {data}")

# 14. Memoryview: View binary content
def view_binary():
    content = memoryview(b"Sample Image Data")
    print(f"Memory view: {content}")
