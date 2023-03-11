for num in range(1, 101):  
    if num % 3 == 0 and num % 5 == 0: # Checks if number is multiple of both 3 and 5
        print("FizzBuzz")
    elif num % 3 == 0: # Checks if number is multiple of 3
        print("Fizz")   
    elif num % 5 == 0: # Checks if number is multiple of 5
        print("Buzz")  
    else:  # If number is not a multiple of 3 or 5
        print(num)