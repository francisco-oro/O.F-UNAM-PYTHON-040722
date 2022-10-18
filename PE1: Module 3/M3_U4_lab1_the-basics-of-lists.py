hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

hat_list[2] = int(input("Give me a number: "))

del hat_list[len(hat_list)-1]
print("Current list length:", len(hat_list))
print(hat_list)
