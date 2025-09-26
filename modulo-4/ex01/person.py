class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        """Inits an object of type Person"""
        self.name = name
        self.age = age

    def birthday(self) -> None:
        """Increments attribute "age" of a Person object"""
        self.age = self.age + 1
