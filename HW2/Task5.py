dayStr,monthStr,yearStr = input("Enter date :").split()
day = int(dayStr)
month = int(monthStr)
year = int(yearStr)

leapYear = (year % 4 ==0) and (year % 100 !=0) or (year % 400 ==0)
valid = day > 0 and day < 32 and month > 0 and month < 13 and ((month==1) or 
                                                            (month == 2 and (
     (day <30 and leapYear == True) or (day < 29 and leapYear == False))) or month == 3)
