class Grandparent:
    height = 170
    satiety = 100
    age = 60


class Parent(Grandparent):
    age = 40


class Child(Parent):
    height = 50

    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)


evelina = Child()
