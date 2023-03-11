num = int(input("Enter an integer: ")) # Takes user input

print("Factors of", num, "are:") # Finds and prints factors of the number
for i in range(1, num + 1):
    if num % i == 0:
        print(i)