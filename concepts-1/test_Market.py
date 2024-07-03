import logging

from exercises1 import Circle, Dog

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("test_Market")


def test_Circle():
    c1 = Circle(3)
    c1.radius = 10
    assert c1.radius == 10


def test_Dog():
    print("Dog test")
    dog_jack = Dog(name="Jack", age=1)
    dog_bear = Dog(name="Bear", age=3)
    assert dog_bear.name == "Bear"
    assert dog_bear.species == "Canis familiaris"
    assert dog_bear.age == 3
    print(str(dog_bear) + "\n")
    print(str(dog_jack) + "\n")
