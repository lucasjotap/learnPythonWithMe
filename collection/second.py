# Collection: Counter, namedTuple, orderedDict, defaultDict, deque.
from collections import Counter

a = "aaaaabbbbccccc"

my_counter = Counter(a)

print(my_counter)
print(list(my_counter.elements()))
x = list(my_counter.elements())
counter = 0
for i in x:
    counter = counter + 1
    if counter >= 14:
        print("Target reached %i" % counter)