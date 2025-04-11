# Let's use the age_calculator example

import datetime

#requesting user's input
year = input("Enter your year of birth: ")

#let's check the type for year
print(type(year))

#fetching the current year
current_year = datetime.date.today().year


# the type for year is 'str' so to avoid the TypeError
# you have to convert the type to int as shown below
age = current_year - int(year)

#printing the user's age
print("You are " + str(age) + " years old!")