List = [45, 33 , 33 , 45 , 21]
print(len(List))

# print unique items
set1 = set(List)
print(set1)
t = ("The testing academy","for","the testing academy")
print("\n set with the use of tuple:")
print(set1)

set1 = {1,2,3}
set2 = {4,5,6}

my_set = set1.union(set2)
print(my_set)


set1 = {1 , 2 , 3 , 4 , 5 }
set2 = {4,5 , 6 , 7 , 8 }

my_set= set1.difference(set2)
print(my_set)

set1 = {1,2 , 4 , 3 , 5}
set2 = {4 , 6 , 3}
subset =set2.issubset(set1)
print(subset)

# l1 = {1,2, 3, 4, 5}
#l2 = {1, 2,3 ,4,5}
# l3 = l1