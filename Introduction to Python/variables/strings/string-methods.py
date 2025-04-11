language = "Obviously, Python is the best!"

# 1. len()
print(language.__len__())

# the code above shows another way of using the method (len) which calculates
# the length of the string

# 2. upper() and lower()
print(language.upper())
print(language.lower())

# 3. find()
# the code below looks for the index for the first lowercase o
print(language.find('o'))

# 3a. in operator
# the code below checks if the searched character is available
print('best' in language)
print('Best' in language)

#the code below looks for the index for the first uppercase o
print(language.find('O'))

# 4. replace()
# the code below first looks for the word/character to be replaced
# and replace it with the new ome
print(language.replace('Python','Java'))