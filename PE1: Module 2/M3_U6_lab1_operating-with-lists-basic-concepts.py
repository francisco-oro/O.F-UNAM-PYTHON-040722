my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []
for number in my_list: 
    if number in newList:
        continue
    newList.append(number)
print("The list with non-repeating elements:")
print(newList)
