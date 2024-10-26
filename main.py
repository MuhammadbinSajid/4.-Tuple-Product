# Function to calculate the product of all numbers in a tuple
def calculate_product(input_tuple):
    product = 1  # Initialize product to 1
    for number in input_tuple:
        product *= number  # Multiply each number
    return product

# Example tuple
numbers_tuple = (20, 6, 5, 10)

# Calculate the product
result = calculate_product(numbers_tuple)

# Print the result
print("The product of all numbers in the tuple is:", result)
