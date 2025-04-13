num = 20
def multiply_by_10(n):
    n = 10
    num = n # changing the value inside the function

    print("value of num inside functions ",num)
    return n
op = multiply_by_10(num)
print(op)
print("value of num outside function",num)
