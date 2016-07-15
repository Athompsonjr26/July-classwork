# OOP Phrase Drills

This is a slightly modified version of http://learnpythonthehardway.org/book/ex41.html

## The Drills

Code: class X(Y)
English: Make a class named X that inherits Y.

Code:

class X(object):
  def __init__(self, J)

English: class X has-a __init__ that takes self and J parameters.


Code:

class X(object):
  def M(self, J)

English: class X has-a function named M that takes self and J parameters.

Code: foo = X()
English: Set foo to an instance of class X.

Code: foo.M(J)
English: From foo get the M function, and call it with parameters self, J.

Code: foo.K = Q
English: From foo get the K attribute and set it to Q.
