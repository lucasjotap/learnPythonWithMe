my_dict = dict(name="Maddie", age=17, city="Lisbon")

# Copying dictionaries wihtout affecting original.
my_dict_two = my_dict.copy()
my_dict_three = dict(my_dict)

my_dict_two["name"] = "Madson"
my_dict_three["name"] = "Marylin"

print(my_dict)
print(my_dict_two)
print(my_dict_three)