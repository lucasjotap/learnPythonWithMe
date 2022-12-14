set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_b = {1, 2, 3, 10, 11, 12}


# intersection_update() allows you to retrieve a set of existing elements in both sets.
# set_a.intersection_update(set_b)

# difference_update() allows you to retrieve a set of unmatched elements in both sets.
# set_a.difference_update(set_b)

set_a.symmetric_difference_update(set_b)

print(set_a)