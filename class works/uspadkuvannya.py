# батьківський клас
class Human:
    height = 170
    satiety = 50


# дочірний клас
class Student(Human):
    height = 150
    satiety = 0

# дочірний клас
class Worker(Human):
    satiety = 100



nazar = Student()
dima = Worker()

print(f"Nazar height {nazar.height}  satiety {nazar.satiety}")
print(f"Dima height {dima.height} satiety {dima.satiety}")






