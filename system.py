from person import Salesman, Buyer
from car import Car
from rent import RentCar

class RentalSystem:
    def __init__(self, cars=[], salesman=[], buyers=[]):
        self.cars = cars
        self.salesman = salesman
        self.buyers = buyers
    
    def create_buyer(self):
        self.buyers.clear()
        print("Buyer datails: ")
      
        name  = input("Name: ")
        surname = input("Surname: ")
        country = input("Country: ")
    
        
        buyer = Buyer(name, surname, country)
        self.buyers.append(buyer)

    def create_employe(self):
        print("New sellers detail to hire")
        name = input("Name: ")
        surname = input(" Surname: ")
        id_shop = input ("ID of shop: ")

        new_employer = Salesman(name, surname, id_shop)
        self.salesman.append(new_employer)

    def create_car(self):
        print("New car details: ")
        brand = input("Car brand : ")
        type = input("car type: ")
        color = input("Car color: ")

        car = Car(brand, type, color)
        self.cars.append(car)

    def choice_sales(self):
        print("Choice your salesman: ")
        counter = 0
        for sales in self.salesman:
            print (f"{counter}, {sales}")
            counter = counter + 1
        user_choice = int(input("Plese, choose your salesman: ""\n"))
        print(f"Your seller: {self.salesman[user_choice]}, will be here at the moment.")
    
    def create_rent(self):
        counter = 0
        print("Choise your car for rent")
        
        for rent in (self.cars):
            print(f"{counter}. {rent}")
            counter = counter + 1
        user_choice_car = int(input("Please, choose your car for rent: ""\n"))
        buyer = self.buyers[0]
        rent_car = RentCar(buyer,self.cars[user_choice_car])
        self.cars.pop(user_choice_car)
        print(rent_car)

system = RentalSystem(
    salesman=[Salesman("Milan", "Novák", 125),
              Salesman("Petr", "Hucko", 85),
                          ],
    cars=[Car("Toyta", "SUV", "Red"),
          Car("Škoda", "Superb", "White"),])