def is_palindrome(s):
    # Convert the string to lowercase and remove spaces
    s = s.lower().replace(" ", "")
    
    # Check if the reversed string is the same as the original string
    return s == s[::-1]
my_string = "A man a plan a canal Panama"
result = is_palindrome(my_string)
print(result) # Output: True


#if spaces and cases are taken into consideration

# def is_palindrome(s):
#     # Remove spaces and convert to lowercase
#     s = s.replace(" ", "")
    
#     # Compare the reversed string to the original string
#     return s == s[::-1]
