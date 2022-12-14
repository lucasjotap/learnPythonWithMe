my_dict_two = dict(name="Maddie", age=17, city="Lisbon")

# print(my_dict_two["name"])
my_dict_two["phone"] = "305 302 302"

for key, value in my_dict_two.items():
    print(key + ":" + str(value))