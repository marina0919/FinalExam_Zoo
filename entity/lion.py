from entity.animal import Gender, CarnivoreAnimal


class Lion(CarnivoreAnimal):
    def __init__(self, name='NoName', gender=Gender.Male, weight=5, eats_per_day=1, teeth_length=1):
        super().__init__(weight, eats_per_day, teeth_length)
        self.__name = name
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @name.setter
    def name(self, name):
        self.__name = name

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    def __str__(self):
        gender_str = "Male" if self.gender == Gender.Male else "Female"
        return (
                f"Lion: name = {self.name}, " +
                f"gender = {gender_str}, " +
                super().__str__()
        )
