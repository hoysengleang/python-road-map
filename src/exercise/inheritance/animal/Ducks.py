from Animal import Animal
from Dogs import Dogs


class Duck(Animal):

    def __init__(self, name, species)-> None:
        super().__init__(name, species)


    def make_sound(self):
        return "Quack"








if __name__ == "__main__":
    dog = Dogs("Buddy", "Dog")
    duck = Duck("Daffy", "Duck")
    print(dog.name, dog.species, dog.make_sound())
    print(duck.name, duck.species, duck.make_sound())