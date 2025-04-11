# In this example, I want to calculate age.
# I imported the datetime library so that I can fetch the current year
# we are in.
import datetime

#requesting user's input
year = input("Enter your year of birth: ")

#fetching the current year
current_year = datetime.date.today().year

#calculating age
age = current_year - int(year)

#printing the user's age
print("You are " + str(age) + " years old!")
