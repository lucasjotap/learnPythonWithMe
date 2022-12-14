set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_b = {1, 2, 3}

# Here we check if a set is a subset of another set. A subset occurs when all the elements of a set can ben found in another set, no matter their size.
# print(set_a.issubset(set_b))
# print(set_b.issubset(set_a))
print(set_b.issuperset(set_a))
print(set_a.issuperset(set_b))