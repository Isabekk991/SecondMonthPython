class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        print(f"color changed from {self.color} to {new_color}")
        self.color = new_color




class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        super().__init__(the_model,the_year,the_color)
       



class Car(Transport):
    def __init__(self, the_model, the_year, the_color, penalties=0):
        super().__init__(the_model,the_year,the_color)
        self.penalties = penalties


    def drive(self, city):
        print(f'car {self.model} is driving to {city}')


    def signal(self, num_of_time, sound):
        while num_of_time > 0:
            print(f"Car {self.model} is signalling: {sound}")
            num_of_time -= 1


class Truck(Car):
    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model,the_year,the_color,penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, weight, product_type):
        if weight > self.load_capacity:
            print(f"You can not load more than {self.load_capacity} kg.")
        else:
            print(f"You successfully loaced the cargo of {product_type} ({weight}kg.)")




number = 5
my_car = Car("BMW X6", 2020, "Black")
print(my_car)
print(f'MODEL: {my_car.model} YEAR: {my_car.year} COLOR:{my_car.color}'
      f'PENALTIES: {my_car.penalties}')


best_car = Car(penalties=900, the_year=2021, the_model="Honda Fit", the_color="Blue")
print(f'MODEL: {best_car.model} YEAR: {best_car.year} COLOR:{best_car.color} '
      f"PENALTIES: {best_car.penalties}")
# best_car.color = "Red"
best_car.change_color("Red")
print(f'MODEL: {best_car.model} YEAR: {best_car.year} NEW COLOR:{best_car.color} '
      f"PENALTIES: {best_car.penalties}")

my_car.drive("Osh")
best_car.drive("Kant")
best_car.drive("Tokmok")
best_car.signal(3,"Beep")

my_plane = Plane("Boeing 747",2019,"White")
print(F"MODEL: {my_plane.model} YEAR: {my_plane.year} COLOR: {my_plane.color}")

truck = Truck("Volvo 300", 2000, "Blue", 500, 30000)
print(f"MODEL: {truck.model} YEAR: {truck.year} COLOR: {truck.color}"
      f"PENALTIES: {truck.penalties} LOAD CAPACITY: {truck.load_capacity}")

truck.load_cargo(35000, "apples")
truck.load_cargo(25000, "oranges")
truck.drive("batken")

print('end of Program')

