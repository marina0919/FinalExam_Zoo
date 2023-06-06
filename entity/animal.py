import enum


# Using enum class create enumerations
class Gender(enum.Enum):
    Male = 1
    Female = 2


class Animal:
    def __init__(self, weight=5):
        if isinstance(weight, (int, float)) and weight > 0:
            self.weight = weight
        else:
            self.weight = 5

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if isinstance(weight, (int, float)) and weight > 0:
            self.__weight = weight

    def __str__(self):
        return f"weight = {self.__weight} kg"


# animal who eat only grass
class HerbivoreAnimal(Animal):
    def __init__(self, weight=0, eats_per_day=0):
        super().__init__(weight)
        self.eats_per_day = eats_per_day

    @property
    def eats_per_day(self):
        return self.__eats_per_day

    @eats_per_day.setter
    def eats_per_day(self, eats_per_day):
        if isinstance(eats_per_day, (int, float)) and eats_per_day > 0:
            self.__eats_per_day = eats_per_day

    def __str__(self):
        return (
                f"eats_per_day = {self.__eats_per_day} kg of grass, " +
                super().__str__()
        )


# animal who eat only meat
class CarnivoreAnimal(Animal):
    def __init__(self, weight=5, eats_per_day=1, teeth_length=1):
        super().__init__(weight)
        if isinstance(eats_per_day, (int, float)) and eats_per_day > 0:
            self.eats_per_day = eats_per_day
        else:
            self.eats_per_day = 1

        if isinstance(teeth_length, (int, float)) and teeth_length > 0:
            self.teeth_length = teeth_length
        else:
            self.teeth_length = 1

    @property
    def teeth_length(self):
        return self.__teeth_length

    @teeth_length.setter
    def teeth_length(self, teeth_length):
        if isinstance(teeth_length, (int, float)) and teeth_length > 0:
            self.__teeth_length = teeth_length

    @property
    def eats_per_day(self):
        return self.__eats_per_day

    @eats_per_day.setter
    def eats_per_day(self, eats_per_day):
        if isinstance(eats_per_day, (int, float)) and eats_per_day > 0:
            self.__eats_per_day = eats_per_day

    def __str__(self):
        return (
                f"eats_per_day = {self.eats_per_day} kg of meat, " +
                f"teeth_length = {self.teeth_length} sm, " +
                super().__str__()
        )
