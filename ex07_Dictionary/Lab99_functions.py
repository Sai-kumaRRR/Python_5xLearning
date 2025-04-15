numbers = [1 , -2 , -3 , -4 , -5 , -6 , -7 , -8 , -9 , -10]

def is_positive(num):
    return num>0
# 2| 10| 5

# 10
 #----
 # 0
positive_numbers = filter(is_positive,numbers)
print(positive_numbers)
positive_numbers_list = list(positive_numbers)
print(positive_numbers_list)