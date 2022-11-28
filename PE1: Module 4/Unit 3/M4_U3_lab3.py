def is_year_leap(year):
    if(year % 4 != 0): return False
    if(year % 100 != 0): return True
    return (True if year % 400 == 0 else False)

def days_in_month(year, month):
    daysperMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(month < 1 or month > 12): return None
    if(is_year_leap(year) is True): daysperMonth[1] += 1
    return daysperMonth[month - 1]    

def day_of_year(year, month, day):
    daysperMonth = []
    sum = 0 
    for i in range(1, month): sum += days_in_month(year, i)
    sum += day
    return sum
print(day_of_year(2000, 12, 31))