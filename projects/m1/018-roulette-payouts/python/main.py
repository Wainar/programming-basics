import random

def spin_roulette():
    return random.randint(0, 36)  # Generate a random number between 0 and 36

def check_color(number):
    if number == 0 or number == 00:
        return "Green"
    elif number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        return "Red"
    else:
        return "Black"

def check_odd_even(number):
    if number in [0, 00]:  # 0 and 00 do not pay out for even
        return "Doesn't pay for even"
    elif number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check_range(number):
    if number in range(1, 19):
        return "1 to 18"
    elif number in range(19, 37):
        return "19 to 36"

# Simulate a spin
result = spin_roulette()

# Display the outcome
print(f"The spin resulted in {result}...")

# Pay the single number
print(f"Pay {result}")

# Pay based on color
print(f"Pay {check_color(result)}")

# Pay based on odd or even
print(f"Pay {check_odd_even(result)}")

# Pay based on range
print(f"Pay {check_range(result)}")
