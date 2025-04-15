# order dictionary

my_dict = {'a':1,'b':2 ,'c':3}
print(my_dict)
val = (my_dict.pop('a'))
print(val)
# print(my_dict.pop('b'))
# print(my_dict.pop('c'))

print(my_dict)

my_dict['a'] = val
print(my_dict)

# key - value pairs based on the order of insertion
# list , se , tuple , dict , ordered  dict - API automation and selenium

od = ordered.Dict()
od['a'] =45
od['c'] =78
od['d'] =56
od['b'] =49

print(od)
#selenium - insert the web elements into a dict
# you want to keep the order - login elements , dashboard elements.
# dict - it will not keep the order of insertion .
# ordered dict - it will keep the order of insertion

keys = list(od.keys())
print(keys)
keys_sort = keys.sorted(keys)
print(keys_sort)
keys_sort_rev= list(reversed(keys))
print(keys_sort_rev)
od2 = ordered.Dict()
od2[keys_sort[0]] = 45
od2[keys_sort[1]] = 78
od2[keys_sort[2]] = 56
od2[keys_sort[2]] = 49

print(od2)


