year = int(input("Enter year : "))

leapYear = (year % 4 == 0) and (year % 100 !=0) or (year % 400 == 0)
print("Leap year :",leapYear)

