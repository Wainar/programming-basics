# Define a function called 'day_of_week' that calculates the day of the week for January 1 of a given year.
def day_of_week(year):
    # Calculate the day number using the provided formula.
    day_number = (year + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400) % 7
    
    # Define a list containing the names of the days of the week.
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    # Return the name of the day corresponding to the calculated number.
    return days_of_week[day_number]

# Ask the user to input the year.
year = int(input("Enter the year: "))

# Call the 'day_of_week' function with the input year and assign the result to the variable 'day'.
day = day_of_week(year)

# Print the result.
print(f"The day of the week on January 1, {year} is {day}.")