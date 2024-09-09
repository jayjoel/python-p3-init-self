#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed

ric = Dog('ric')
print(ric.breed)

snoopy = Dog('snoopy', "Mtina")
print(snoopy.breed)