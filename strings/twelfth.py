# Formating strings.
var = "Cat"
var1 = 10
var2 = 5.0

my_string = "The variable is %s" % var
interger_string = "The variable is %i" % var1
float_string = "The variable is %.3f" % var2

print(my_string)
print(interger_string)
print(float_string)

new_string = "The variable is {}".format(var)
new_string = "The variable is {}".format(var1)
new_string = "The variable is {:.2f}".format(var2)
new_string = "The variable is {:.2f} and {}".format(var2, var)

print(new_string)