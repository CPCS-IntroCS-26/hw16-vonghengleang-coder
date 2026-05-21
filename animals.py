class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}!")

    def move(self):
        print(f"{self.name} moves around.")

    def describe(self):
        print(f"{self.name} is a {self.age}-year-old {self.__class__.__name__}.")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__}, {self.age} years old.)"


class Dog(Animal):
    def __init__(self, name, age, sound, breed):
        super().__init__(name, age, sound)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks {self.sound}.")

    def move(self):
        print(f"{self.name} runs on four legs.")


class Bird(Animal):
    def __init__(self, name, age, sound, can_fly):
        super().__init__(name, age, sound)
        self.can_fly = can_fly 
    
    def move(self):
        if self.can_fly:
            print(f"{self.name} flies through the air.")
        else:
            print(f"{self.name} walks on the ground.")

class Fish(Animal):
    def __init__(self, name, age, sound, water_type):
        super().__init__(name, age, sound)
        self.water_type = water_type
    
    def move(self):
        print(f"{self.name} swims in the water.")


class Cat(Animal):
    def __init__(self, name, age, sound, indoor):
        super().__init__(name,age, sound)
        self.indoor = indoor
    
    def speak(self):
        print(f"{self.name} meow {self.sound}!")
    
    def move(self):
        print(f"{self.name} sneaks quietly.")
