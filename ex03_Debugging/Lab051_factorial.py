number = int(input("enter the number\n"))
if number < 0:
    print("factorial is not possible !! from negative")
else:
    fact = 1
    for i in range(1, number + 1):  # 0 len-1)
        fact = fact * i
        print("fact is -> ", fact)
