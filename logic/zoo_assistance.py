from container.zoo import Zoo
from entity.animal import CarnivoreAnimal, HerbivoreAnimal


class ZooAssistance:
    @staticmethod
    def calculate_total_weight_of_meat(zoo):
        if isinstance(zoo, Zoo) and zoo.size != 0:
            total_meat_per_day = 0
            for i in range(zoo.size):
                animal = zoo.get_animal(i)

                if isinstance(animal, CarnivoreAnimal):
                    total_meat_per_day += animal.eats_per_day

            return total_meat_per_day
        else:
            return 0

    @staticmethod
    def calculate_total_weight_of_grass(zoo):
        if isinstance(zoo, Zoo) and zoo.size != 0:
            total_grass_per_day = 0
            for i in range(zoo.size):
                animal = zoo.get_animal(i)

                if isinstance(animal, HerbivoreAnimal):
                    total_grass_per_day += animal.eats_per_day

            return total_grass_per_day
        else:
            return 0

    @staticmethod
    def find_animal_max_eat_meat(zoo):
        if isinstance(zoo, Zoo) and zoo.size != 0:
            food_max_eat_meat = 0
            animal_target = None
            for i in range(zoo.size):
                animal = zoo.get_animal(i)

                if isinstance(animal, CarnivoreAnimal) and animal.eats_per_day > food_max_eat_meat:
                    animal_target = animal
                    food_max_eat_meat = animal_target.eats_per_day

            return animal_target
        else:
            return None

    @staticmethod
    def find_animal_max_eat_grass(zoo):
        if isinstance(zoo, Zoo) and zoo.size != 0:
            food_max_eat_per_day = 0
            animal_target = None
            for i in range(zoo.size):
                animal = zoo.get_animal(i)

                if isinstance(animal, HerbivoreAnimal) and animal.eats_per_day > food_max_eat_per_day:
                    animal_target = animal
                    food_max_eat_per_day = animal_target.eats_per_day

            return animal_target
        else:
            return None
