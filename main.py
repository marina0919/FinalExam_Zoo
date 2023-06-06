from container.zoo import Zoo
from entity.animal import Gender
from entity.lion import Lion
from entity.tiger import Tiger
from entity.zebra import Zebra
from logic.zoo_assistance import ZooAssistance


def main():
    zoo = Zoo()

    mufasa = Lion(name='Mufasa', gender=Gender.Male, weight=190.0, eats_per_day=10)
    simba = Lion(name='Simba', gender=Gender.Male, weight=30.0, eats_per_day=2)
    nala = Lion(name='Nala', gender=Gender.Female, weight=135.0, eats_per_day=5)
    scar = Lion(name='Scar', gender=Gender.Male, weight=120.0, eats_per_day=4)

    shere_khan = Tiger(name='Shere Khan', gender=Gender.Male, weight=250.0, eats_per_day=15)
    diego = Tiger(name='Diego', gender=Gender.Male, weight=300.0, eats_per_day=25)

    zebra = Zebra(scientific_name='Equus zebra', gender=Gender.Male, weight=300.0, eats_per_day=46)
    zebra_hartmannae = Zebra(scientific_name='Equus zebra hartmannae', gender=Gender.Male, weight=320.0,
                             eats_per_day=57)

    zoo.add(mufasa)
    zoo.add(simba)
    zoo.add(nala)
    zoo.add(scar)
    zoo.add(shere_khan)
    zoo.add(diego)
    zoo.add(zebra)
    zoo.add(zebra_hartmannae)

    total_meat_weight = ZooAssistance.calculate_total_weight_of_meat(zoo)
    total_grass_weight = ZooAssistance.calculate_total_weight_of_grass(zoo)
    animal_max_eat_meat = ZooAssistance.find_animal_max_eat_meat(zoo)
    animal_max_eat_grass = ZooAssistance.find_animal_max_eat_grass(zoo)

    total_food_stat = (f"Total products count for the Zoo per day:\n" +
                       f"Meat: {total_meat_weight} kg\n" +
                       f"Grass: {total_grass_weight} kg\n\n" +
                       f"Total products count for the Zoo per month:\n" +
                       f"Meat: {total_meat_weight * 31} kg\n" +
                       f"Grass: {total_grass_weight * 31} kg\n\n")

    if animal_max_eat_meat is None:
        meat_eater_msg = "Zoo haven't carnivore Animals\n"
    else:
        meat_eater_msg = f"Max meat eater:\n{animal_max_eat_meat}\n"

    if animal_max_eat_grass is None:
        grass_eater_msg = "Zoo haven't herbivore Animals\n"
    else:
        grass_eater_msg = f"Max grass eater:\n{animal_max_eat_grass}\n"

    print(
        f"{zoo}\n\n" +
        total_food_stat +
        meat_eater_msg +
        "\n" +
        grass_eater_msg
    )


if __name__ == "__main__":
    main()
