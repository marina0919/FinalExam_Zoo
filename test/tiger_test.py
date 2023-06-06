import unittest

from entity.animal import Gender
from entity.tiger import Tiger


class TigerTest(unittest.TestCase):
    def test_tiger_default_constructor(self):
        tiger = Tiger()
        expected_name = 'NoName'
        expected_gender = Gender.Male
        expected_weight = 5
        expected_eats_per_day = 1

        self.assertEqual(expected_name, tiger.name)
        self.assertEqual(expected_gender, tiger.gender)
        self.assertEqual(expected_weight, tiger.weight)
        self.assertEqual(expected_eats_per_day, tiger.eats_per_day)

    def test_tiger_constructor_with_args(self):
        expected_name = "Tiger"
        expected_gender = Gender.Female
        expected_weight = 200
        expected_eats_per_day = 15

        tiger = Tiger(expected_name, expected_gender, expected_weight, expected_eats_per_day)

        self.assertEqual(expected_name, tiger.name)
        self.assertEqual(expected_gender, tiger.gender)
        self.assertEqual(expected_weight, tiger.weight)
        self.assertEqual(expected_eats_per_day, tiger.eats_per_day)

    def test_negative_tiger_weight(self):
        weight = -200
        expected = 5

        tiger = Tiger(weight=weight)

        self.assertEqual(expected, tiger.weight)

    def test_negative_tiger_eats_per_day(self):
        eats_per_day = -2
        expected = 1

        tiger = Tiger(eats_per_day=eats_per_day)

        self.assertEqual(expected, tiger.eats_per_day)

    def test_zero_tiger_weight(self):
        weight = 0
        expected = 5

        tiger = Tiger(weight=weight)

        self.assertEqual(expected, tiger.weight)

    def test_zero_tiger_eats_per_day(self):
        eats_per_day = 0
        expected = 1

        tiger = Tiger(eats_per_day=eats_per_day)

        self.assertEqual(expected, tiger.eats_per_day)

    def test_tiger_gender(self):
        gender = Gender.Female
        expected = Gender.Female

        tiger = Tiger(gender=gender)

        self.assertEqual(expected, tiger.gender)

    def test_weight_property_negative(self):
        tiger = Tiger()
        expected = tiger.weight
        tiger.weight = -200
        self.assertEqual(expected, tiger.weight)

    def test_weight_property_positive(self):
        tiger = Tiger()
        expected = 200
        tiger.weight = 200
        self.assertEqual(expected, tiger.weight)

    def test_weight_property_with_zero(self):
        tiger = Tiger()
        expected = tiger.weight
        tiger.weight = 0
        self.assertEqual(expected, tiger.weight)

    def test_eats_per_day_property_negative(self):
        tiger = Tiger()
        expected = tiger.eats_per_day
        tiger.eats_per_day = -200
        self.assertEqual(expected, tiger.eats_per_day)

    def test_eats_per_day_property_positive(self):
        tiger = Tiger()
        expected = 2000
        tiger.eats_per_day = 2000
        self.assertEqual(expected, tiger.eats_per_day)

    def test_eats_per_day_property_with_zero(self):
        tiger = Tiger()
        expected = 1
        tiger.eats_per_day = 0
        self.assertEqual(expected, tiger.eats_per_day)


if __name__ == "__main__":
    unittest.main()
