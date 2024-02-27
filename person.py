
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname =surname
        

class Salesman(Person):
    def __init__(self, name, surname, id_shop):
        super().__init__(name, surname)
        self.id_shop = id_shop

    def __str__(self):
        return f"Salesman, name {self.name} {self.surname}, his ID {self.id_shop}"

class Buyer (Person):
    def __init__(self, name, surname, country):
        super().__init__(name, surname) 
        self.country = country 
    def __str__(self):
        return f"{self.name} {self.surname}, from {self.country}"


