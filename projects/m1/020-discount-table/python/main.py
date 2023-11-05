# List of original prices
original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]

# Display table headers
print("{:<15} {:<15} {:<15}".format("Original Price", "Discount", "New Price"))

# Loop through each original price
for price in original_prices:
    # Calculate the discount (60% off)
    discount = price * 0.60
    
    # Calculate the new price after discount
    new_price = price - discount
    
    # Display the values with 2 decimal places
    print("${:<14.2f} ${:<14.2f} ${:<.2f}".format(price, discount, new_price))
