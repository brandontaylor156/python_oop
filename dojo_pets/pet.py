class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 20
        self.energy = 20

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        if self.type == "dog":
            print("Woof!")
        elif self.type == "cat":
            print("Meow!")
        else:
            print("Whattup tho?!")
        return self

class Dog(Pet):
    def __init__(self, name, type, tricks, bark_volume):
        super().__init__(name, type, tricks)
        self.bark_volume = bark_volume

    def noise(self):
        print("Woof!")
        return self

class Cat(Pet):
    def __init__(self, name, type, tricks, lives):
        super().__init__(name, type, tricks)
        self.lives = lives

    def noise(self):
        print("Meow!")
        return self

