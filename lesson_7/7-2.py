from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def my_stuff(self):
        pass

class Coat(Clothes):

    def __init__(self, size):
        self.V = size

    @property
    def my_stuff(self):
        return self.V / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.H = height

    @property
    def my_stuff(self):
        return 2 * self.H + 0.3

c = Coat(44)
print(c.my_stuff)
s = Suit(175)
print(s.my_stuff)
total = round(c.my_stuff + s.my_stuff)
print(total)
