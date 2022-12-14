# Lists: ordered, mutable, allows duplicate elements.
from tkinter import Y


my_list_one = ["banana", "apple", "cherry"]

my_list_two = [10] * 10

x = my_list_one + my_list_two

print(x)

print(x[:3])

y = x[:]

print(y)