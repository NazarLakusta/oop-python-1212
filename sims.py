from random import *


class Human:
    def __init__(self, name, job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return

        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")

        else:
            if self.satiety >= 100:
                self.satiety = 100
                return

            self.satiety += 5
            self.food -= 5

    def work(self):

        if self.car.drive():
            pass

        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return

            else:
                self.to_repair()
                return

        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass

        else:
            if self.car.fuel < 20:
                manage = "fuel"

            else:
                self.to_repair()
                return

        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100

        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50

        elif manage == "delicacies":
            print("Hoorrayy! Delicious!")
            self.gladness+=10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def days_index(self, day):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass


class Auto:
    def __init__(self, brand_list):
        self.brand = choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):

        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True

        else:
            print("The car cannot move")
            return False


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "Photoshop creator": {"salary": 30, "gladness_less": 25},
    "C++ creator": {"salary": 60, "gladness_less": 30},
}
