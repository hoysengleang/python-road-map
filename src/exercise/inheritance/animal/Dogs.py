from Animal import Animal

class Dogs(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def make_sound(self):
        return "Woof"