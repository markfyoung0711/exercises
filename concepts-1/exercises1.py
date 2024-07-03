import logging
import time

from decorators import debug, do_twice, timer

log = logging.getLogger(name="__file__")


@do_twice
@debug
def do(i: int, j: int):
    """multiply i * j and return results"""
    return i * j


@timer
def mine(list1: list):
    for _ in list1:
        time.sleep(1)
        log.info("sleeping 1 second")
    return True


if __name__ == "__main__":
    result = mine(list(range(0, 10)))
    # result = do(2, 3)
    log.info(f"{result} is result")


# Classes
class Marketplace(object):
    def __init__(self):
        pass


class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius, fset=_set_radius, fdel=_del_radius, doc="The radius property."
    )


class Animal(object):
    def __init__(self, age, species, says=""):
        self._age = age
        self._species = species
        self._says = says

    def _set_species(self, value):
        self._species = value

    def _get_species(self):
        return self._species

    def _set_age(self, value):
        self._age = value

    def _get_age(self):
        return self._age

    def speak(self):
        return self._says

    species = property(fset=_set_species, fget=_get_species)
    age = property(fset=_set_age, fget=_get_age)


class Dog(Animal):

    def __init__(self, name, age, says="Ruff!"):
        super().__init__(age=age, species="Canis familiaris", says=says)
        self._name = name

    def _set_says(self, value):
        self._says = value

    def _get_says(self):
        return self._says

    def _set_name(self, name):
        self._name = name

    def _get_name(self):
        return self._name

    def __str__(self):
        return f"Animal.Dog\nName: {self._name}\nAge: {self._age}\nSays: {self._says}"

    def speak(self):
        return self._says

    name = property(fset=_set_name, fget=_get_name)
    says = property(fset=_set_says, fget=_get_says)
