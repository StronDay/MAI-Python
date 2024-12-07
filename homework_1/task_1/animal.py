# -*- coding: utf-8 -*-

class Animal:
    
    def __init__(self, name):
        self.name = name
        self.sound = ""

    def makesound(self):
        print(self.name)
        
class Cat(Animal):
    
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def makesound(self):
        super().makesound()
        print("Мяу Мяу")

class Dog(Animal):
    
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def makesound(self):
        super().makesound()
        print("Гав Гав")
        

animal = Animal("Обычное животное")

cat = Cat("Барсик", "Серый")
dog = Dog("Граф", "Фиолетовый")

cat.makesound()
dog.makesound()

print("Цвет кота: " + cat.color)
print("Цвет собаки: " + dog.color)