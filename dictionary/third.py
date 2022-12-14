my_dict_two = dict(name="Maddie", age=17, city="Lisbon")

print(my_dict_two)

del my_dict_two["name"]
my_dict_two.pop("city")
my_dict_two.popitem()
print(my_dict_two)