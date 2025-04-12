# Map and fitter in the list
sq=lambda x: x*x
result = sq(5)
print(result)
# map functions (where we sill go from one item and apply)
numbers = [1 , 2 , 3 , 4 , 5]
sq_number = []
for i in numbers:
    sq_number.append(sq(i))
    print(sq_number)
    # map function
    sq_number2 = list(map(lambda x:x**numbers))
    print(sq_number2)
