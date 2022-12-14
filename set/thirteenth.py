set_a = {1, 2, 3, 4, 5, 6}

set_b = set_a # This doesnt make an indepedent copy

set_b.add(10)

set_c = set_a.copy()
set_c.add(11)
set_d = set(set_a)
print(set_a)
print(set_c)
print(set_d)