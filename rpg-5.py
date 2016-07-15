"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

#make a class named Character that inherits object
class Character(object):
#method named alive that takes self as a parameter
    def alive(self):
        return self.health > 0
#method named attack that takes self and enemy as a parameter
    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
#from time get the sleep method and call it with parameters self and 1.5
        time.sleep(1.5)
#method named receive_damage that takes self and points as a parameter
    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name
#method named print_status that takes self as a parameter
    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)
# Make a class named Hero that inherits Character
class Hero(Character):
# class named Hero has a dunder-init that takes self as parameters
    def __init__(self):
# From self get the name attribute and set it to hero
        self.name = 'hero'
# From self get the health attribute and set it to 10
        self.health = 10
# From self get the power attribute and set it to 5
        self.power = 5
# From self get the coin attribute and set it to 20
        self.coins = 20
#class Hero has has a method named restore that takes self as parameter
    def restore(self):
# From self get the health attribute and set it to goblin
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
#From time get the sleep method and call it with parameter self, 1
        time.sleep(1)
#class Hero has has a method named buy that takes self and item as parameter
    def buy(self, item):
        self.coins -= item.cost
#From item get the apply method and call it with parameter self, hero
        item.apply(hero)
# Make a class named Goblin that inherits Character
class Goblin(Character):
# class named Goblin has a dunder-init that takes self as parameters
    def __init__(self):
# From self get the name attribute and set it to goblin
        self.name = 'goblin'
# From self get the health attribute and set it to 6
        self.health = 6
# From self get the power attribute and set it to 2
        self.power = 2
# make a class named Wizard that inherits self as parameters
class Wizard(Character):
# class named wizard has a dunder-init that takes self as parameters
    def __init__(self):
# From self get the name attribute and set it to wizard
        self.name = 'wizard'
# From self get the health attribute and set it to 8
        self.health = 8
# From self get the power attribute and set it to 1
        self.power = 1
#class wizard has a method named attack that takes self, enemy as parameter
    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power
# make a class named Battle that inherits self as parameters
class Battle(object):
# class Battle has a method named do_battle that takes self, hero and enemy as parameters
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
#From hero get the print_status method and call it with parameter self
            hero.print_status()
#From enemy get the print_status method and call it with parameter self
            enemy.print_status()
#From time get the sleep method and call it with parameter self, 1.5
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
#From hero get the attack method and call it with parameter self, enemy
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
#From enemy get the attack method and call it with parameter self, hero
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False
# make a class named Tonic that inherits object as parameters
class Tonic(object):
    cost = 5
    name = 'tonic'
# class Tonic has a method named apply that takes self, character and as parameters
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)
# make a class named Sword that inherits object as parameters
class Sword(object):
    cost = 10
    name = 'sword'
# class Sword has a method named apply that takes self, character and as parameters
    def apply(self, character):
        character.power += 2
        print "%s's power increased to %d." % (character.name, character.power)
# make a class named Shopping that inherits object as parameters
class Shopping(object):
    items = [Tonic, Sword]
# class Shopping has a method named do_shopping that takes self, hero as parameters
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Shopping.items)):
                item = Shopping.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Shopping.items[input - 1]
#set items to an instance of class ItemToBuy
                item = ItemToBuy()
#
                hero.buy(item)

hero = Hero()
enemies = [Goblin(), Wizard()]
battle_engine = Battle()
shopping_engine = Shopping()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
