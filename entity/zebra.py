from entity.animal import Gender, HerbivoreAnimal


class Zebra(HerbivoreAnimal):
    def __init__(self, scientific_name='NoName', gender=Gender.Male, weight=0, eats_per_day=0):
        super().__init__(weight, eats_per_day)
        self.__scientific_name = scientific_name
        self.__gender = gender

    @property
    def scientific_name(self):
        return self.__scientific_name

    @property
    def gender(self):
        return self.__gender

    @scientific_name.setter
    def scientific_name(self, scientific_name):
        self.__scientific_name = scientific_name

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    def __str__(self):
        gender_str = "Male" if self.gender == Gender.Male else "Female"
        return (
                f"Zebra: scientific_name = {self.scientific_name}, " +
                f"gender = {gender_str}, " +
                super().__str__()
        )
