my_dict ={'a':1,'b':2,'c':3,'d':4}

print(my_dict)
#IF you have duplicate key,latest value of key will be used!
keys = my_dict.keys()
values = my_dict.values()

# GET all the keys into a list
keys_list = list(keys)
print(values)
print(keys_list[0])
print(keys_list[1])
print(keys_list[2])

my_dict ={'a':1,'b':2,'c':3,'d':4}

#Dict -key and value
my_dict.clear()
print(my_dict)
copy_my_dict = my_dict.copy()
print(copy_my_dict)