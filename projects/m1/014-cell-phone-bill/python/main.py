# Define constants
BASE_CHARGE = 15.00
MINUTES_INCLUDED = 50
MESSAGES_INCLUDED = 50
ADDITIONAL_MINUTE_COST = 0.25
ADDITIONAL_MESSAGE_COST = 0.15
fee_911 = 0.44
TAX_RATE = 0.05

# Get user input
minutes_used = int(input("Input minutes: "))
messages_used = int(input("Input messages: "))

# Calculate additional charges
extra_minutes_charge = max(0, minutes_used - MINUTES_INCLUDED) * ADDITIONAL_MINUTE_COST
extra_messages_charge = max(0, messages_used - MESSAGES_INCLUDED) * ADDITIONAL_MESSAGE_COST

# Calculate total charges
subtotal = BASE_CHARGE + extra_minutes_charge + extra_messages_charge + fee_911
tax = subtotal * TAX_RATE
total = subtotal + tax

# Display results
print(f"Base charge: {BASE_CHARGE:.2f}€")
if extra_minutes_charge > 0:
    print(f"Extra minutes charge: {extra_minutes_charge:.2f}€")
if extra_messages_charge > 0:
    print(f"Extra messages charge: {extra_messages_charge:.2f}€")
print(f"911 fee: {fee_911:.2f}€")
print(f"Tax: {tax:.2f}€")
print(f"Total bill amount: {total:.2f}€")
