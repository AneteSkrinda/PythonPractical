def even_value_keys(d):
    result = []
    for key, value in d.items():
        if value % 2 == 0:
            result.append(key)
    return result
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
even_keys = even_value_keys(my_dict)
print(even_keys)  # Output: ['b', 'd']
