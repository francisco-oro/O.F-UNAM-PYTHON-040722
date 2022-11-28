def is_year_leap(year):
    if(year % 4 != 0): return False
    if(year % 100 != 0): return True
    return (True if year % 400 == 0 else False)

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
