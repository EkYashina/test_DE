class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Kennel:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_animal_names(self):
        return [animal.name for animal in self.animals]

# Создаем объекты
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Labrador")

# Создаем объект Kennel
kennel = Kennel()

# Добавляем объекты в список в Kennel
kennel.add_animal(dog1)
kennel.add_animal(dog2)

# Выводим список имен всех животных в Kennel
print(kennel.get_animal_names())


