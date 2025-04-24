class Car:
    name = "Sai"  # class Variables


print("I will be called first")


def start_engine(self):
    print("Starting a car", self.make, self.model)
    Car1 = Car("Toyota", "civic")
    Car2 = Car("Honda", "camry")

    Car1.start_engine(),
    Car2.start_engine()
    print(id(Car1))
    print(id(Car2))
