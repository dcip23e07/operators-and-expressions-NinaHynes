# Exercise: Comparison Operator
#
var_a = 1500 + 3000
var_b = 1500 + 3000.00
var_c = "4500"
var_d = 4500.000001
var_e = 1000
var_f = 5000 - 500
var_g = 60000

# Print out the following values in your script
# i. var_a == var_b
# ii. var_a >= var_b
# iii. var_a > var_b
# iv. var_a > var_c
# v. var_a > var_d
# vi. var_g < var_b
# vii. var_a != var_c
# viii. var_e == var_f

print(var_a == var_b)
print(var_a >= var_b)
print(var_a > var_b)
# print(var_a > var_c) #cannot print this as TypeError: '>' not supported between instances of 'int' and 'str'
print(var_a > var_d)
print(var_g < var_b)
print(var_a != var_c)
print(var_e == var_f)

# True
# True
# False
# False
# False
# True
# False
