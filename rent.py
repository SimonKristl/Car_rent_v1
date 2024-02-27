
class RentCar:
    def __init__(self, buyer = [], cars = []):
        self.cars = cars
        self.buyer = buyer

    def add_car(self, car):
        self.cars.append(car)

    def __str__(self):
        return f"Your car {self.cars} is prepared for drive! Thank you Mr/Mrs {self.buyer}"