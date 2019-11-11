class Dog:
    def __init__(self):
        print("woof woof")

    def pee(self):
        print("I will pee")


class Puppy(Dog):
    def __init__(self):
        super().__init__()
        print("im tiny")


p = Puppy()
