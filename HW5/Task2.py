def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
my_string = "hello world"
num_vowels = count_vowels(my_string)
print(num_vowels) # Output: 3