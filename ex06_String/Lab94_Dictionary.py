my_dict = {'a': 1,'b':2,'c':3}
# val = my_dict.pop('a')
# print(val)

# pop items() is used to remove and return an arbitrary

# from the dictionary

val = my_dict.popitem()
print(val)
print(my_dict)
del my_dict
print(my_dict)
