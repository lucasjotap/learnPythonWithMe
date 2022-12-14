set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_b = {1, 2, 3, 10, 11, 12}

# The difference method will allow you to see the different elements between sets.
diff = set_a.difference(set_b)
another_diff = set_b.difference(set_a)
print(diff)
print(another_diff)