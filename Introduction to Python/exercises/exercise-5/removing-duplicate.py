num = [2,2,4,6,3,4,6,1]
uniques = []

for item in num:
    # this iteration, only adds a number which is not already in uniques
    if item not in uniques:
        uniques.append(item)
print(uniques)