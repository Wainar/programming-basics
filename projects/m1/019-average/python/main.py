def get_user_input():
    values = []
    
    while True:
        value = float(input("Enter a value (or 0 to exit): "))
        
        if value == 0:
            break
        else:
            values.append(value)
    
    return values

def calculate_average(values):
    total = sum(values)
    count = len(values)
    return total / count if count > 0 else None

# Get values from the user
user_values = get_user_input()

# Check if the first value is 0
if len(user_values) > 0 and user_values[0] == 0:
    print("Error: The first value cannot be 0.")
else:
    # Calculate and display the average
    average = calculate_average(user_values)
    if average is not None:
        print(f"The average of the entered values is: {average}")
    else:
        print("No values entered.")
