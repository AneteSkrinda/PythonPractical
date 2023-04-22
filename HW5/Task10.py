def swap_first_last(t):
    if len(t) < 2:
        return t
    else:
        return (t[-1],) + t[1:-1] + (t[0],)
my_tuple = (1, 2, 3, 4, 5)
swapped_tuple = swap_first_last(my_tuple)
print(swapped_tuple)  # Output: (5, 2, 3, 4, 1)
