num = [5,2,1,2,7,4]

#append method adds the item to the last index
num.append(20)
print(num)

# insert method adds the item with the ability to specify the index
num.insert(0, 10)
print(num)

# remove method removes an item from the list
num.remove(5)
print(num)

#pop method removes the last item in the list
num.pop()
print(num)

# count method checks the number of occurance of an itme in the list
print(num.count(2))

# sort method sorts the items in ascending order
num.sort()
print(num)

# copy method replicates the list to another list
num2 = num.copy()
print(f"new list: {num2}")

# reverse method reverses the list
num.reverse()
print(num)

# clear method removes all items in the list
num.clear()
print(num)