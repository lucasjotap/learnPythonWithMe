from re import I


my_set = set()

my_set.add(1)
my_set.add(3)
my_set.add(2)

my_set.remove(3)

# clear(), pop() and remove() can be used on sets.

my_set.add(4)


print(my_set)

for i in my_set:
    print(i)