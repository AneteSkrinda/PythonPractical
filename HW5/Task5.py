def find_sum_pair(numbers, target_sum):
    seen = {}
    for num in numbers:
        difference = target_sum - num
        if difference in seen:
            return [difference, num]
        seen[num] = True
    return None
numbers = [2, 5, 7, 11, 13]
target_sum = 18
result = find_sum_pair(numbers, target_sum)
print(result)  # Output: [7, 11]
