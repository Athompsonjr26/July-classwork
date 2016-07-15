"""
The hero now has to first fight the goblin, and then fight the wizard in order to win.
"""
import random
import time

class Character(object):
    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

hero = Hero()
enemies = [Goblin(), Wizard()]

for enemy in enemies:
    print "====================="
    print "Hero faces the %s" % enemy.name
    print "====================="
    while hero.alive() and enemy.alive():
        hero.print_status()
        enemy.print_status()
        time.sleep(1.5)
        print "-----------------------"
        print "What do you want to do?"
        print "1. fight %s" % enemy.name
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            hero.attack(enemy)
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            exit(0)
        else:
            print "Invalid input %r" % input
        enemy.attack(hero)
    if hero.alive():
        print "You defeated the %s" % enemy.name
        hero.restore()
    else:
        print "YOU LOSE!"
        exit(0)

print "YOU WIN!"
