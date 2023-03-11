age = int(input("Enter your age:"))
if age > 17:
    hasDrivingLicense = input("Do you have a driving license (y/n)?")

result = age >=18 and hasDrivingLicense == "y"
if result:
    print("You are able to drive :" + str(result))


if not result:
    print("You are able to drive : " + str(result))
    
   