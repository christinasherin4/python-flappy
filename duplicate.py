num1 = [2,2,4,6,3,4,6,1]
uniques = []
for number in num1:
    if number not in uniques:
        uniques.append(number)
print(uniques)