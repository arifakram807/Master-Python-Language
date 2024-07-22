# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""
# Your Code Below:

class Animals:
    counter=0
    def __init__(self):
        print('animal created')
        Animals.counter+=1
    def move(self_):
        print('animal is moving')
    def eat(self):
        print('its eating')
    def countanimal(self):
        print(Animals.counter)
class Dog(Animals):
    def __init__(self,dog_name,dog_age):
        Animals.__init__(self)
        self.Dog_name=dog_name
    def move(self):
        print('dog is walking')
class Fish(Animals):
    def __init__(self,fish_name,fish_age):
        Animals.__init__(self)
        self.Fish_name=fish_name
        self.Fish_age=fish_age
    def move(self):
        print('fish is swiming')
class Bird(Animals):
    def __init__(self,bird_name,bird_age):
        Animals.__init__(self)
        self.Bird_name=bird_name
        self.Bird_age=bird_age
    def move(self):
        print('birds are flying')


bird1=Bird('peacock',10)
bird1.move()
bird1.eat()
bird1.countanimal()
fish1=Fish('joja',2)
fish1.move()
fish1.eat()
fish1.countanimal()


















































# Solution:
# class Animal:
#     def __init__(self):
#         print("Animal Constructed")
#
#     def move(self):
#         print("Animal Moving...")
#
#     def eat(self):
#         print("Animal Eating...")
#
#
#
# class Bird(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Bird flying...")
#
#
#
# class Fish(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Fish Swimming...")
#
#
# class Dog(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Dog Running ...")
#
# mydog = Dog(3, "wolfy")
# mydog.move()
# mydog.eat()
#
# mydog = Fish(1, "nemo")
# mydog.move()
# mydog.eat()
#
# mydog = Bird(3, "jojo")
# mydog.move()
# mydog.eat()