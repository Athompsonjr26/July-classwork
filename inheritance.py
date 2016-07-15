class Animal(object):
    def breed(self):
        return Animal()

# Cat is a subclass of Animal
# Animal is the parent class (or base class) of Cat
# Cat is-a Animal
# Cat inherits all things (methods, attributes) from Animal
class Cat(Animal):
    def meow(self):
        print 'Meow!'

my_cat = Cat()
my_cat.meow()
kitten = my_cat.breed()

class Dog(Animal):
    def woof(self):
        print 'Woof!'

class Pomeranian(Dog):
    def woof(self):
        print 'WOOOOOOOOF!'

class Person(Animal):
    def greet(self):
        print 'Hello!'

    def breed(self):
        return Person()

# type
# isinstance()
