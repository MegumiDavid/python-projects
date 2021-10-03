class Animal():

    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale & Exhale")


class Fish(Animal):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def breathe(self):
        super().breathe()
        print("Under the water")

    def swim(self):
        print("Swimming ~~~")


nemo = Fish("Angel Fish")
print(nemo.name)
print(nemo.eyes)
nemo.breathe()
nemo.swim()


class Dog:
    def __init__(self):
        self.temperament = "loyal"


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"


class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.is_a_good_boy = True

    def bark(self):
        super().bark()
        print("Greetings, good sir. How do you do?")