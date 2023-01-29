class Human:
    def __init__(self, name="Human"):
        self.name = name

    def __str__(self):
        return f"My name {self.name}"

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers(self):
        if self.passengers:
            print(f"Names of {self.brand} passengers")
            for el in self.passengers:
                print(el)
            else:
                print(f"There are no passengers in {self.brand}")

porsh = Auto('porsh')
ferari = Auto('ferari')


oleg = Human(name='oleg')
ben = Human('ben')

porsh.add_passengers(oleg)
porsh.add_passengers(ben)

porsh.print_passengers()