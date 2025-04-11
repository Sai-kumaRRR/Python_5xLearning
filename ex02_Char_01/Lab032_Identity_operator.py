# Identity operator
# is returns true if both variables  are the same object
# is not  returns true if both variables  are not same object.
# * = # identity operator

x = [1,2,3]
y = [5,6,7]
print(x is y)
print(id(x))
print(id(y))
print(y is x)
print(x is not y)
