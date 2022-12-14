# Tuple: ordered, immutable, allows duplicate elements.
import sys
my_list = [0, 1, 2, "hellow", True]
x = tuple(my_list)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(x), "bytes")

import timeit

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=100000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=100000000))