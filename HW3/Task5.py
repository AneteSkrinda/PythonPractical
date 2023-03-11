num = int(input("Enter an integer: ")) # Takes user input

is_prime = True # Checks if number is prime
if num < 2:
    is_prime = False
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break

if is_prime: # Prints result
    print(num, "is prime")
else:
    print(num, "is not prime")