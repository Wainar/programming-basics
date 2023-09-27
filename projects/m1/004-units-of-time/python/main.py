days = int(input("Type the days of your choice: "))

hours = int(input(" Type the hours: "))

minutes = int(input(" Type the minutes "))

seconds = int(input(" type the seconds: "))

def units_of_time(days,hours,minutes,seconds):
    number_days = days * 86400
    number_hours = hours * 3600
    number_minutes = minutes * 60
    return number_days + number_hours + number_minutes 

print(" The total amount of seconds are: "+ str(units_of_time(days, hours, minutes, seconds)) + ("s"))    
