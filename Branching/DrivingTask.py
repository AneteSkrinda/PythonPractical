age = int(input("Enter your age:"))
if age > 17:
    hasDrivingLicense = input("Do you have a driving license (y/n)?")

result = age >=18 and hasDrivingLicense == "y"
if result:
    print("You are able to drive")
    print("Congratulations")

#print("THIS CODE WILL ALWAYS BE PRINTED")

if not result:
    print("You are not able to drive")
    print("It's sad!")

