year = int(input("Input a year: "))

if year < 1582: print("Not within the gregorian calendar period")
elif year % 4 != 0 : print("Normal year")
elif year % 100 != 0 : print("Leap year")
elif year % 400 != 0 : print("Normal year")
else: print("Leap year")
