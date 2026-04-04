class Dog:
    # Class variable (common for all dogs)
    animal = "Dog"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def display(self):
        print("Animal:", Dog.animal)
        print("Breed:", self.breed)
        print("Name:", self.name)
        print("---------------------")


# Create objects of two different breeds
dog1 = Dog("Labrador", "Buddy")
dog2 = Dog("German Shepherd", "Max")

dog1.display()
dog2.display()