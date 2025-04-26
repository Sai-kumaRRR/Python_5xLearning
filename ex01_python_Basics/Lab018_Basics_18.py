# String
# Bunch of Char
name = "Sai"
name2 = "Kumar"
# String Functions
# Python String Input able in Nature -> They can't change! one created
# name[0] = "n" type Error: "Str" object does not support item assignment
# Capitalize()
# Returns. copy of the String with its first character capitalize.

result = name.capitalize()
print(result)
print(name)
#Upper case
result2 = name.Upper()
print(result2)
#Lower case
result3 = name.lower()
print(result3)
print(id(result3))   # Identity - address reference

#Swap case()
# Returns a copy of the String with upper case characters converted to lower case
# And vice

print(name.swapcase())

# Tittle
# return a little cased version of the String
# Where words start with an uppercase Character and
# The remaining Characters are lower case

name = "Hello World"
print(name.Tittle(1))

t1 = "Kumar"
t2 = "Sai"
print(t1.Captialize())
print(t2.Upper())

#t1 is ref or variable name, "Kumar" which is stored i memory
name= "Kumar"
text = "Hello World"
result_ref = text.replace
print(result_ref)
#index and len
name = "sai"
# len-1
print(len(name))
# index -> 0 to len-1
# p -0 , r -1 , a -2 , m- 3 , o-4 , d -5
# Find ()
# returns the lowest index of a sub String in the String
# Returns -1 if the sub String is not found.

text = " Hello World"
index = text.find("World")
print(index)
# Count()- count the CharCount = text.Count('l')print(Count)
name = "S I"
print(len(name))
name = "Sai"
print(name)
del(name)
print(name)

