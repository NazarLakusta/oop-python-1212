def function():
    pass

class Student:

    # метод ініціалізації
    def __init__(self,name,height):
        self.name = name
        self.height = height



    def print_info(self):
        print(f"I'm Alive my name is: {self.name}")
        print(f"My height {self.height} cm \n")




student_Nazar = Student("Nazar",173)

# виклик методу класу
student_Nazar.print_info()


student_Max = Student("Max",210)
student_Max.print_info()






