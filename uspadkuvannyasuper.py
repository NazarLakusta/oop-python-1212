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
