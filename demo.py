from hsekat.Park import Park
from hsekat.models.Technic import *
from hsekat.models.Thing import *
from hsekat.container import create_container


def main():
    container = create_container()
    park = container.resolve(Park)

    samokat = Samokat("S1", "Самокат", 8, True, 1.2)
    bike = Bike("B1", "Велосипед", 7, True)
    samokat_break = Samokat("S2", "Самокат сломан", 9, False, 1.5)

    for technic in (samokat, bike, samokat_break):
        print(technic.name, park.success_technic(technic))

    park.register_thing(Helmet("H1", "Шлем"))
    park.register_thing(ChargeWardrobe("C1", "Зарядный шкаф", 2.5))

    print(f"Количество техники: {park.technic_count}")
    print(f"Количество вещей: {park.thing_count}")
    print(f"Общее количество: {park.general_count}")
    print(f"Энергия: {park.general_energy_use()}")

    for technic in park.technics_beginner():
        print(technic.name)
    for item in park.all_inventory():
        print(item.inventory_number, item.name)

if __name__ == "__main__":
    main()
