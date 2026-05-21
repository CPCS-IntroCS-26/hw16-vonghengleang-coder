from animals import Animal, Dog, Bird, Fish, Cat

def main():
    animals = [
        Dog("Gavin", 2, "woof", "husky"),
        Bird("Liam", 3, "cheep", True),
        Fish("Malie", 1, "sss", "ocean"),
        Cat("Adam", 5, "meow", True)
    ]

    for animal in animals:
        animal.speak()
        animal.move()
        animal.describe()
        print()


if __name__ == "__main__":
    main()
