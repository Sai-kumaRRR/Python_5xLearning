numbers = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
# num2 == 0
even_numbers = [2 , 4 , 6 ,8 , 10]
# filter -> numbers element can be less or equal the list

def is_even(num):
    return num %2 ==0

# modulus
# 2 | 3 ||
# 2
# -----
# 1

even_numbers = filter(is_even,numbers)
print(even_numbers)
even_numbers_list = list(even_numbers)
print(even_numbers_list)