
class Car:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def __str__(self):
        return f"{self.brand}, type {self.type} and color is {self.color}"