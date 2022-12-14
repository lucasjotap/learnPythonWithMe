# Lists: ordered, mutable, allows duplicate elements.
my_list = ["banana", "apple", "cherry"]

my_list_two = list() # Creates an empty list. 

# Select items in a list by selecting its index.
item = my_list[2]
# print(item)
# print(my_list[-1])

# Insert method allows you to insert an item at a specific location in a list.
my_list.insert(0, "blackberry")

# Iterate through a list.
# for fruit in my_list:
#     if (fruit != "cherry"):
        # print(fruit)

# Append to list.
my_list.append("lemon")
# print(my_list)

# Creating a list copy
my_list_three = my_list

# Popping last element of my_list copy
x = my_list_three.pop()

# print(my_list_three)
# print(x)


