from timeit import default_timer as timer

# Checking for time equality for each way of joining strings.
my_list = ['a'] * 1000000

start = timer()
my_string = ""
for i in my_list:
    my_string += i
stop = timer()
print(stop-start)

# Join method is more efficient.
start = timer()
x = " ".join(my_list)
print(stop-start)

# Join method joins every item in a list into a string.
y = "".join(my_list)
