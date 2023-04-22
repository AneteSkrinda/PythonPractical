def quicksort(arr):
    # Base case: an empty or one-element array is already sorted
    if len(arr) < 2:
        return arr
    
    # Choose a pivot element (we'll use the first element for simplicity)
    pivot = arr[0]
    
    # Partition the array into two sub-arrays
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    # Recursively sort the sub-arrays and concatenate them with the pivot
    return quicksort(left) + [pivot] + quicksort(right)

my_list = [5, 2, 8, 1, 9, 3]
sorted_list = quicksort(my_list)
print(sorted_list) # Output: [1, 2, 3, 5, 8, 9]
