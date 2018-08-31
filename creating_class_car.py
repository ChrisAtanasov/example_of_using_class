class Car:

    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color

    def car(self):
        return f"Cars usually can be separated by{self.brand}, {self.model} and color{self.color}"


new_car=Car("Lamborghini","Aventador","White")

print(f"I think that everyone will like a brandnew {new_car.brand} ")
print(f"The one that all we like is {new_car.model}")
print(f"Probably will be looking good in a {new_car.color} color.")


old_car=Car("Lamborghini","Aventador","Yellow")

print(f"Sometimes we dont hove so much money for new car, but we can buy a old {old_car.brand} ")
print(f"We can buy also a used {old_car.model}")
print(f"The color which we like is {old_car.color}")