class Human:
    def __init__(self,name,height,age,color_hair):
        self.name = name
        self.height = height
        self.age = age
        self.color_hair = color_hair

    def info(self):
        print(f"Human info:"
              f"\nName: {self.name}"
              f"\nHeight: {self.height}"
              f"\nAge: {self.age}"
              f"\nColor hair: {self.color_hair}")


class Worker(Human):

    def __init__(self,name,height,age,color_hair, salary, position, experience):
            super().__init__(name,height,age,color_hair)

            self.salary = salary
            self.position = position
            self.experience = experience

    def info(self):
        super().info()
        print(f"\nWorker info:"
              f"\nSalary: {self.salary}"
              f"\nPosition: {self.position}"
              f"\nExperience: {self.experience}")


nazar = Human("Nazar",175,21,"Black")
nazar.info()
print()
ruslan = Worker("Ruslan",180,13,"Brown",1,"Potuzhnist",1)
ruslan.info()