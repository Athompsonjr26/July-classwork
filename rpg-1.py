"""
Same game as rpg-1.py, except that we extracted the Hero and Goblin as classes.
The logic for attack() has been extracted into the classes and the main loop just
has to call attack().
"""

class Hero(object):
    def __init__(self):
        self.health = 10
        self.power = 5

    def alive(self):
        return self.health > 0

    def attack(self, goblin):
        if not self.alive():
            return
        goblin.health -= self.power
        print "You do %d damage to the goblin." % self.power
        if goblin.health <= 0:
            print "goblin is dead."

    def print_status(self):
        print "You have %d health and %d power." % (self.health, self.power)

class Goblin(object):
    def __init__(self):
        self.health = 6
        self.power = 2

    def alive(self):
        return self.health > 0

    def attack(self, hero):
        if not self.alive():
            return
        hero.health -= self.power
        print "goblin does %d damage to you." % self.power
        if hero.health <= 0:
            print "hero is dead."

    def print_status(self):
        print "The goblin has %d health and %d power." % (self.health, self.power)

hero = Hero()
goblin = Goblin()

while hero.alive() and goblin.alive():
    hero.print_status()
    goblin.print_status()
    print
    print "What do you want to do?"
    print "1. fight goblin"
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()
    if input == "1":
        hero.attack(goblin)
    elif input == "2":
        pass
    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input
    goblin.attack(hero)
