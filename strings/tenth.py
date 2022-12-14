from timeit import default_timer as timer

my_list = ['a'] * 6
print(my_list)

start = timer()
my_string = ""
for i in my_list:
    my_string += i
stop = timer()
print(stop-start)

start = timer()
print(" ".join(my_list))
print(stop-start)
print("".join(my_list))
