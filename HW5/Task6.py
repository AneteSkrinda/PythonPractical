def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
numbers = [1, 2, 3, 4, 5]
product = calculate_product(numbers)
print(product)  # Output: 120 (i.e., 1 * 2 * 3 * 4 * 5)
