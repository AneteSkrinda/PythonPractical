def filter_not_divisible_by_3(s):
    return {x for x in s if x % 3 != 0}
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
filtered_set = filter_not_divisible_by_3(my_set)
print(filtered_set)  # Output: {1, 2, 4, 5, 7, 8}
