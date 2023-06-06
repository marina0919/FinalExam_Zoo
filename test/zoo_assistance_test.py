import unittest

from container.zoo import Zoo
from entity.animal import CarnivoreAnimal, HerbivoreAnimal
from entity.lion import Lion
from entity.zebra import Zebra
from logic.zoo_assistance import ZooAssistance


class ZooAssistanceTest(unittest.TestCase):
    def test_01_different_type(self):
        zoo = "string"
        expected = 0

        actual = ZooAssistance.calculate_total_weight_of_meat(zoo)

        self.assertEqual(expected, actual)

    def test_02_calculate_total_products_count_of_meat_with_empty_zoo(self):
        zoo = Zoo()
        expected = 0

        actual = ZooAssistance.calculate_total_weight_of_meat(zoo)

        self.assertEqual(expected, actual)

    def test_03_calculate_total_products_count_of_grass_with_empty_zoo(self):
        zoo = Zoo()
        expected = 0

        actual = ZooAssistance.calculate_total_weight_of_grass(zoo)

        self.assertEqual(expected, actual)

    def test_04_calculate_total_products_count_of_meat_with_zoo_None(self):
        zoo = None
        expected = 0

        actual = ZooAssistance.calculate_total_weight_of_meat(zoo)

        self.assertEqual(expected, actual)

    def test_05_calculate_total_products_count_of_grass_with_zoo_None(self):
        zoo = None
        expected = 0

        actual = ZooAssistance.calculate_total_weight_of_grass(zoo)

        self.assertEqual(expected, actual)

    def test_06_zoo_with_products_positive(self):
        animal1 = CarnivoreAnimal(eats_per_day=5)
        animal2 = CarnivoreAnimal(eats_per_day=10)
        animal3 = CarnivoreAnimal(eats_per_day=3)

        zoo = Zoo()
        zoo.add(animal1)
        zoo.add(animal2)
        zoo.add(animal3)

        expected = 18

        actual = ZooAssistance.calculate_total_weight_of_meat(zoo)

        self.assertEqual(expected, actual)

    def test_07_zoo_with_one_carnivore_animal(self):
        animal = Lion(eats_per_day=5)

        zoo = Zoo()
        zoo.add(animal)

        expected = animal.eats_per_day

        actual = ZooAssistance.calculate_total_weight_of_meat(zoo)

        self.assertEqual(expected, actual)

    def test_08_calculate_total_products_count_of_grass_with_one_carnivore_animal(self):
        animal = Lion(eats_per_day=5)

        zoo = Zoo()
        zoo.add(animal)

        expected = 0

        actual = ZooAssistance.calculate_total_weight_of_grass(zoo)

        self.assertEqual(expected, actual)

    def test_09_calculate_total_products_count_of_grass_with_one_herbivore_animal(self):
        animal = Zebra(eats_per_day=5)

        zoo = Zoo()
        zoo.add(animal)

        expected = animal.eats_per_day

        actual = ZooAssistance.calculate_total_weight_of_grass(zoo)

        self.assertEqual(expected, actual)

    def test_10_zoo_with_carnivore_animals__positive(self):
        animal1 = CarnivoreAnimal(eats_per_day=5)
        animal2 = CarnivoreAnimal(eats_per_day=10)
        animal3 = CarnivoreAnimal(eats_per_day=3)
        animal4 = HerbivoreAnimal(eats_per_day=3)

        zoo = Zoo()
        zoo.add(animal1)
        zoo.add("string")
        zoo.add(animal2)
        zoo.add(animal3)
        zoo.add(animal4)
        zoo.add(5)

        expected = 18

        actual = ZooAssistance.calculate_total_weight_of_meat(zoo)

        self.assertEqual(expected, actual)

    def test_11_zoo_with_herbivore_animals__positive(self):
        animal1 = CarnivoreAnimal(eats_per_day=5)
        animal2 = CarnivoreAnimal(eats_per_day=10)
        animal3 = CarnivoreAnimal(eats_per_day=3)
        animal4 = HerbivoreAnimal(eats_per_day=3)

        zoo = Zoo()
        zoo.add(animal1)
        zoo.add("string")
        zoo.add(animal2)
        zoo.add(animal3)
        zoo.add(animal4)
        zoo.add(5)

        expected = 3

        actual = ZooAssistance.calculate_total_weight_of_grass(zoo)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
