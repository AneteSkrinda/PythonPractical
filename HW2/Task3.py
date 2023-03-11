intStr,int2Str = input("Enter two integers :").split()
int1 = int(int1Str)
int2 = int(int2str)
int1Mod = int1 % 2
int2Mod = int2 % 2

print("Both numbers are even :",int1Mod == 0 and int2Mod == 0)
print("At least one number is even : ",int1Mod == 0 or int2Mod == 0)


#print("At least one number is even : ",not (int1Mod != 0 and int2Mod !=0))