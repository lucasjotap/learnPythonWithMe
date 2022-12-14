my_dict_two = dict(name="Maddie", age=17, city="Lisbon")

# Accessing keys in a dictionary
if "last" in my_dict_two:
    print(my_dict_two)

try:
    print(my_dict_two["name"])
except:
    print("Errors")

try:
    print(my_dict_two["lastName"])
except:
    print("Error!")