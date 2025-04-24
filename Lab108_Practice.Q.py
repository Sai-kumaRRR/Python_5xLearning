# Take a input from user we will create how .

class Car:
    Color = None
    Model = None

    def Car_details(self):
        print("your car details is",self.Color,self.Model)
Car_color = input("Enter you car color")
Car_model = input("Enter you car model")



car_obj_ref = Car()
car_obj_ref.color = Car_color
car_obj_ref.Model= Car_model

# obj ref we can call the function

car_obj_ref.Car_details()

#  car_details()



