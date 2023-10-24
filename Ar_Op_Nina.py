# Exercise: Arithmetic Operator

# var_a = 1500 + 3000
# var_b = 1500 + 3000.00
# var_c = 1000/5
# var_d = 1200 + "200"
# var_e = "3004" + "996"

var_a = 1500 + 3000
var_b = 1500 + 3000.00
var_c = 1500/5
# var_d = 1200 + "200"
var_e = "3004" + "996"

# Print the result of var_a and var_b 

print(var_a)
print(var_b)

# var_a is an integer, while var_b is a float. 

#what type of object is var_c ?

print(type(var_c))


# what is the value of var_d? 
# print(var_d)
# what happened when you tried to run that expression?
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# var_d is a string. Python does not allow you to add a string to a number. When you try to run this expression, you will get a TypeError.

# what is the value of var_e? and what object is it?

print(var_e)
print(type(var_e))


