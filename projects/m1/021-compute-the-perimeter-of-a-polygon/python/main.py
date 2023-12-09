import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Get the coordinates of the first point
x_first = float(input("Enter the first x-coordinate: "))
y_first = float(input("Enter the first y-coordinate: "))

x_prev, y_prev = x_first, y_first
total_perimeter = 0.0

# Continue getting coordinates until a blank line is entered for x-coordinate
while True:
    x_next_input = input("Enter the next x-coordinate (press Enter to finish): ")

    if x_next_input == '':
        break

    # Get the coordinates of the next point
    x_next = float(x_next_input)
    y_next = float(input("Enter the next y-coordinate: "))

    # Calculate distance and add it to the total perimeter
    distance = calculate_distance(x_prev, y_prev, x_next, y_next)
    total_perimeter += distance

    # Update the previous coordinates for the next iteration
    x_prev, y_prev = x_next, y_next

# Add the distance from the last point back to the first point
total_perimeter += calculate_distance(x_prev, y_prev, x_first, y_first)

# Display the total perimeter of the polygon
print(f"The perimeter of that polygon is {total_perimeter}")
