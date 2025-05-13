class Person:
    def __init__(self,name,age,height):

        #публічний
        self.name = name

        #захищене
        self._age = age

        #приватний
        self.__height = height


    def get_height(self):
        return self.__height

    def set_height(self, new_height):
        if new_height > 35:
            self.__height = new_height

        else:
            print("Ріст занадто низький. Випий растішку!")

    def drink_rastishka(self):
        print(f"{self.name} Випис растішку")
        self.__height += 15

p = Person("Іван",22,180)

print(p.name)
print(p._age)
print(p.get_height())


print("Іван випив растішку")
p.set_height(195)
print(p.get_height())

p.drink_rastishka()
print(p.get_height())


