set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_b = {1, 2, 3, 10, 11, 12}

# symmetric_difference brings a set of the differing elements in a set.
diff = set_b.symmetric_difference(set_a)

print(diff)