#Name: Doris Tran
#Date: September 8, 2022
#Pets Everywhere
#I copied excercise and filled the empty lines with my solution

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother cat
      
#I created another cat that inherited from Cat class
class Oz(Cat):
    def sing(self, sounds):
        return f'{sounds}'
      

#2 Create a list of all of the pets (create 3 cat instances from the above)
      
#I filled in the empty brackets with the 3 cats
my_cats = [Simon('Simon', 11), Sally('Sally', 3), Oz('Oz', 13)]

#3 Instantiate the Pet class with all your cats

#I put the cats in Pets
allcats = Pets(my_cats)

#4 Output all of the cats singing using the my_pets instance

#I called the walk fuction so the program prints the text from Cats
allcats.walk()
