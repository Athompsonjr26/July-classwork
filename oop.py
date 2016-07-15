class Person(object):
    def __init__(self, name):
        self.name = name

    def say_hello(self, subject):
        print "Hello %s, I am %s!" % (subject, self.name)

aditi = Person('Aditi')
aditi.say_hello('Jerry')
