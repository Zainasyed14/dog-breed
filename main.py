class Dog:
    def __init__(self, breed , color):
        self.breed = breed
        self.color = color

    def PrintInfo(self):
        print(self.breed)
        print(self.color)

poodle = Dog("Poodle", "White")
poodle.PrintInfo()
goldret = Dog("Golden Retriver" , "Cream")
goldret.PrintInfo()