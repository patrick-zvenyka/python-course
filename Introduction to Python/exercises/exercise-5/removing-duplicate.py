num = [2,2,4,6,3,4,6,1]
uniques = []

for item in num:
    if item not in uniques:
        uniques.append(item)
print(uniques)