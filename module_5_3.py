from module_5_2 import House1


class House3(House1):
    def __eq__(self, other):  # ==
        if isinstance(other, House3) or isinstance(other, int):
            return self.number_of_floors == other

    def __ne__(self, other):  # !=
        if isinstance(other, House3) or isinstance(other, int):
            return self.number_of_floors != other

    def __lt__(self, other):  # <
        if isinstance(other, House3) or isinstance(other, int):
            return self.number_of_floors < other

    def __gt__(self, other):  # >
        if isinstance(other, House3) or isinstance(other, int):
            return self.number_of_floors > other

    def __le__(self, other):  # <=
        if isinstance(other, House3) or isinstance(other, int):
            return self.number_of_floors <= other

    def __ge__(self, other):  # >=
        if isinstance(other, House3) or isinstance(other, int):
            return self.number_of_floors >= other

    def __add__(self, other):  # +
        if isinstance(other, House3) or isinstance(other, int):
            self.number_of_floors += other
            return self

    def __sub__(self, other):  # -
        if isinstance(other, House3) or isinstance(other, int):
            self.number_of_floors -= other
            return self

    def __radd__(self, other):  # ?
        if isinstance(other, House3) or isinstance(other, int):
            return self.__add__(other)

    def __iadd__(self, other):  # +=
        if isinstance(other, House3) or isinstance(other, int):
            return self.__add__(other)

    def __isub__(self, other):  # -=
        if isinstance(other, House3) or isinstance(other, int):
            return self.__sub__(other)

#  ================================================

h1 = House3('ЖК Эльбрус', 10)
h2 = House3('ЖК Акация', 20)
print(f'({h1}) == ({h2}): {h1 == h2}')
print(f'({h1}) != ({h2}): {h1 != h2}')
print(f'({h1}) <  ({h2}): {h1 < h2}')
print(f'({h1}) >  ({h2}): {h1 > h2}')
print(f'({h1}) <= ({h2}): {h1 <= h2}')
print(f'({h1}) >= ({h2}): {h1 >= h2}')
print(f'({h1}) == 10): {h1 == 10}')
print(f'({h1}) == "ggg"): {h1 == "ggg"}')
print(f'({h1}) + 2 = {h1 + 2}')
print(f'({h1}) - 2 = {h1 - 2}')
print(f'({h1})', '+= 2 = ', end='')
h1 += 2
print(h1)
print(f'({h1})', '-= 2 = ', end='')
h1 -= 2
print(h1)

print('=================================================')
h1 = House3('ЖК Эльбрус', 10)
h2 = House3('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
