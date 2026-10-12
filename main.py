from hsekat.Park import Park
from hsekat.container import create_container
from hsekat.models.Technic import *
from hsekat.models.Thing import *


def read_int(text: str) -> int:
    try:
        return int(input(text))
    except ValueError:
        raise ValueError("Нужно ввести целое число") from None


def read_energy() -> float:
    text = input("Энергопотребление: ").replace(",", ".")
    try:
        energy = float(text)
    except ValueError:
        raise ValueError("Энергопотребление должно быть числом") from None

    if energy < 0:
        raise ValueError("Энергопотребление должно быть неотрицательным")
    return energy


def read_condition() -> bool:
    answer = input("Техника исправна? (да/нет): ").strip().lower()
    if answer == "да":
        return True
    if answer == "нет":
        return False
    raise ValueError("Введите 'да' или 'нет'")


def add_technic(park: Park):
    print("Тип транспорта:")
    print("1. Велосипед")
    print("2. Самокат")
    print("3. Электровелосипед")
    choice = input("Выберите тип: ").strip()
    if choice not in ("1", "2", "3"):
        print("Неизвестный тип транспорта")
        return
    number = input("Инвентарный номер: ").strip()
    name = input("Наименование: ").strip()
    ease = read_int("Простота управления (1–10): ")
    condition = read_condition()
    if choice == "1":
        technic = Bike(number, name, ease, condition)
    elif choice == "2":
        technic = Samokat(number, name, ease, condition, read_energy())
    else:
        technic = ElectricBike(number, name, ease, condition, read_energy())
    if park.success_technic(technic):
        print("Техника прошла техосмотр и добавлена в парк")
    else:
        print("Техосмотр не пройден. Техника не добавлена")


def add_thing(park: Park):
    print("Тип вещи:")
    print("1. Шлем")
    print("2. Док станция")
    print("3. Зарядный шкаф")
    choice = input("Выберите тип: ").strip()
    if choice not in ("1", "2", "3"):
        print("Неизвестный тип вещи")
        return
    number = input("Инвентарный номер: ").strip()
    name = input("Наименование: ").strip()
    if choice == "1":
        thing = Helmet(number, name)
    elif choice == "2":
        thing = DockStation(number, name, read_energy())
    else:
        thing = ChargeWardrobe(number, name, read_energy())
    park.register_thing(thing)
    print("Вещь добавлена в парк")


def show_counts(park: Park):
    print(f"Транспорта: {park.technic_count}")
    print(f"Вещей: {park.thing_count}")
    print(f"Всего объектов: {park.general_count}")


def show_technics_beginner(park: Park):
    technics = park.technics_beginner()
    if not technics:
        print("Подходящего транспорта пока нет")
        return
    for technic in technics:
        print(f"{technic.inventory_number} — {technic.name}, простота: {technic.ease}")


def show_all_inventory(park: Park):
    inventory = park.all_inventory()
    if not inventory:
        print("Парк пока пуст")
        return
    for item in inventory:
        print(f"{item.inventory_number} — {item.name}")


def main():
    container = create_container()
    park = container.resolve(Park)
    while True:
        print("Действие:")
        print("1. Добавить транспорт")
        print("2. Добавить вещь")
        print("3. Показать количество объектов")
        print("4. Показать энергопотребление")
        print("5. Показать транспорт для новичков")
        print("6. Показать весь инвентарь")
        print("0. Выход")
        try:
            choice = input("Выберите действие: ").strip()
            if choice == "1":
                add_technic(park)
            elif choice == "2":
                add_thing(park)
            elif choice == "3":
                show_counts(park)
            elif choice == "4":
                print(f"Энергопотребление: {park.general_energy_use()}")
            elif choice == "5":
                show_technics_beginner(park)
            elif choice == "6":
                show_all_inventory(park)
            elif choice == "0":
                print("До свидания!")
                break
            else:
                print("Неизвестный пункт меню")
        except ValueError as error:
            print(f"Ошибка: {error}")
        except (EOFError, KeyboardInterrupt):
            print("Работа завершена!")
            break


if __name__ == "__main__":
    main()
