from pet import Pet, Dog, Cat

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.bathe()


myNinja = Ninja("Brandon", "Taylor", ["Senzu Beans", "Beggin Strips"], "Dog Food", Pet("Winnie", "Dog", ["Sit", "Spin", "Lay Down"]))
myNinja.walk()

doggy = Dog("Mamba", "Black Lab", ["Spin", "Lay Down", "Shoot"], 99)
ninja2 = Ninja("Kobe", "Bryant", ["Body Armor", "Beef Jerky"], "Dog Food", doggy)

print(doggy.bark_volume)
print(myNinja.pet.health)

