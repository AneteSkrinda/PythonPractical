def sum_dicts(dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            result[key] = result.get(key, 0) + value
    return result
my_dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
summed_dict = sum_dicts(my_dicts)
print(summed_dict)  # Output: {'a': 9, 'b': 12}
