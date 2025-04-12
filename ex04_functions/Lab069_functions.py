def sayHello():
    print("Hello")
    sayHello()

    def Funcwithparam(a):
        return a ** 2

    0 = Funcwithparam(2)
    print(0)

    # Lambda Expression -> now cpoied by the java

    def doubleofme(Value):

    return Value*2


output = lambda value: value * 2
print(output(2))


def sayHello(name):
    print("Hii your name is", name)
    sayHello = lambda name: print("Hi your , name is", name)

    sayHello("SAI")
    sayHello("Lucky")
