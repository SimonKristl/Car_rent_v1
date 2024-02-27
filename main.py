from system import RentalSystem, system
from person import Salesman
from car import Car

def print_customer():
    print("-------------------------------")
    print(" Welcome in our CarRent!")
    print(" 0 create customer detail, for rent.")
    print(" 99 for exit system.")

def print_menu():
    print("-------------------------------")
    print(" Press the keybord for operation")
    print(" 1 For choise seller")
    print(" 2 For choice car")
    print(" 3 Cars in stock")
    print(" 4 For close")
    print(" XXX secret_shop_menu (55) XXX")

def shop_menu():
    print("1 add car to stock")
    print("2 add new employe")
    print("3 close shop_menu")

# system = RentalSystem(
#     salesman=[Salesman("Milan", "Novák", 125),
#               Salesman("Petr", "Hucko", 85),
#                           ],
#     cars=[Car("Toyta", "SUV", "Red"),
#           Car("Škoda", "Superb", "White"),])

while True:
    print_customer()
    user_choice = int(input("Please chose your operation: "))
    if user_choice == 0:
        system.create_buyer()
        while True:
                print_menu()
                user_choice = int(input("Please chose your operation: "))
                    
                if user_choice == 1:
                    system.choice_sales()
                if user_choice == 2:
                    system.create_rent()
                if user_choice == 3:
                    print("Car in stock: ""\n")
                    for car in system.cars:
                        print(car)
                if user_choice == 4:
                    print("Thank you")
                    break
                if user_choice == 55:
                    while True:
                        shop_menu()
                        shop_choice = int(input("Your action: "))
                        if shop_choice == 1:
                            system.create_car()
                        if shop_choice == 2:
                            system.create_employe()
                        if shop_choice == 3:     
                            break
    if user_choice == 99:
        print ("System shuting down")
        break