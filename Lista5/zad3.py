class Animal:
    def make_sound(self):
        return "Animal sound"
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Dog(Animal):
    def make_sound(self):
        return "Woof"
    def move(self):
        return "Moving"

class Fish(Animal):
    def make_sound(self):
        return "Blub"
    def move(self):
        raise NotImplementedError("Fish cannot move on land")

def let_animal_move(animal):
    try:
        return animal.move()
    except NotImplementedError as e:
        return f"Exception caught: {e}"

dog = Dog()
fish = Fish()

print(let_animal_move(dog))
print(let_animal_move(fish))