"""
Merged common code between Hero and Goblin into a Character class. The code that's specialized to Hero or Goblin are implemented as subclasses to Character.
"""

class Character(object):
    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        enemy.receive_damage(self.power)
        print "%s did %d damage to the %s." % (self.name, self.power, enemy.name)

    def receive_damage(self, points):
        self.health -= points
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2

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
    input = raw_input("> ")
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
