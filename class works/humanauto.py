class Human:
    def __init__(self,name):
        self.name = name


class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passenger = []

    def add_passenger(self,human):
        self.passenger.append(human)

    def print_passenger(self):
        if self.passenger != []:
            print(f"Names of {self.brand} passengers")

            for passenger in self.passenger:
                print(passenger.name)

        else:
            print(f"There are no passengers in {self.brand}")

#Human
nazar = Human("Nazar")
maks = Human("Maks")
ruslanpotuzhnist = Human("Potuzhnist")
evelinapotuzhna = Human("Potuzhna")
dimabarabas = Human("Barabas")
nikita = Human("Nikita")

#Auto
bus_Bogdan = Auto("Bogdan Bus")

bus_Bogdan.add_passenger(nazar)
bus_Bogdan.add_passenger(maks)
bus_Bogdan.add_passenger(ruslanpotuzhnist)
bus_Bogdan.add_passenger(evelinapotuzhna)
bus_Bogdan.add_passenger(dimabarabas)
bus_Bogdan.add_passenger(nikita)


bus_Bogdan.print_passenger()