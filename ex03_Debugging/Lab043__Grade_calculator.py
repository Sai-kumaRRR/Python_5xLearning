# Grade Calculator


scale = int(input("enter the num\n"))
grade = None
if scale >= 90 and scale <= 100:
    print("grade is A")
elif scale >= 80 and scale <= 89:
    print("grade is B")
elif scale >= 70 and scale <= 79:
    print("grade is C")
elif scale >= 60 and scale <= 69:
    print("grade id D")
elif scale >= 0 and scale <= 59:
    print("scale is A")

else:
    print("invalid input")
