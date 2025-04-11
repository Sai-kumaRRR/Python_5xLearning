side1 = float(input("enter the length of side1:"))
side2 = float(input("enter the length of side2:"))

side3 = float(input("enter the length of side3:"))

if side1 == side2 == side3:
    print("small")
elif side1 == side3 or side2 == side3 or side1 == side2:
    print("ISO")
else:
    print("scalene")
