class Animal:

    def __init__(self,name):
        
        self.name = name

    @property
    def display_name(self):

        return self.name





if __name__ == "__main__":
    animal = Animal("Buddy")
    print(animal.display_name)