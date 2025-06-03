# match

# similar to switch
number = int(input("enter to number\n"))
match number:
    case 1:
        print("you have entered 1")
    case 2:

        print("you have entered 2")
    case _:  # nothing is matching i will run
        print("no idea")
