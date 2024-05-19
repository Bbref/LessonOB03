import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def eat(self):
        print(f"{self.name} ест")


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} щебечет")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит")


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def show_all_animals(self):
        for animal in self.animals:
            print(f"Животное: {animal.name}, Возраст: {animal.age}")

    def show_all_staff(self):
        for staff_member in self.staff:
            print(f"Сотрудник: {staff_member.name}, должность: {staff_member.position}")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Информация о зоопарке сохранена в {filename}")

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        print(f"Информация о зоопарке загружена из {filename}")
        return zoo


class Staff:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "Зоокипер")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")


# Пример использования
bird = Bird("Попугай", 2, "средний")
mammal = Mammal("Лев", 5, "золотистый")
reptile = Reptile("Змея", 3, "гладкая")

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo_keeper = ZooKeeper("Иван В")
veterinarian = Veterinarian("Доктор Айболит")

zoo.add_staff(zoo_keeper)
zoo.add_staff(veterinarian)

zoo.show_all_animals()
zoo.show_all_staff()

zoo_keeper.feed_animal(mammal)
veterinarian.heal_animal(reptile)

# Сохранение состояния зоопарка в файл
zoo.save_to_file('zoo_data.pkl')

# Загрузка состояния зоопарка из файла
loaded_zoo = Zoo.load_from_file('zoo_data.pkl')
loaded_zoo.show_all_animals()
loaded_zoo.show_all_staff()
