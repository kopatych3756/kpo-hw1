import pytest
from hsekat.Park import Park
from hsekat.interfaces.IInspector import IInspector
from hsekat.models.Technic import *
from hsekat.models.Thing import *
from hsekat.services.ServiceCenter import ServiceCenter

class FakeInspector(IInspector):
    def __init__(self, result: bool):
        self.result = result
        self.checked: list[Technic] = []

    def check(self, technic: Technic) -> bool:
        self.checked.append(technic)
        return self.result


# Проверяем что Park одобрил фейковый сервис
def test_fake_add() -> None:
    inspector = FakeInspector(True)
    park = Park(inspector)
    bike = Bike("B1", "Велосипед", 7, False)

    assert park.success_technic(bike) is True
    assert park.technic_count == 1
    assert park.technics() == (bike,)
    assert inspector.checked == [bike]


def test_fake_not_add() -> None:
    inspector = FakeInspector(False)
    park = Park(inspector)
    scooter = Samokat("S1", "Самокат", 8, True, 1.2)

    assert park.success_technic(scooter) is False
    assert park.technic_count == 0
    assert park.all_inventory() == ()
    assert park.general_energy_use() == 0.0
    assert inspector.checked == [scooter]


def test_thing() -> None:
    inspector = FakeInspector(False)
    park = Park(inspector)
    park.register_thing(Helmet("H1", "Шлем"))

    assert park.thing_count == 1
    assert inspector.checked == []


def test_duplicate() -> None:
    park = Park(FakeInspector(True))
    park.success_technic(Bike("B1", "Велосипед", 7, True))

    with pytest.raises(ValueError, match="уже занят"):
        park.register_thing(Helmet("B1", "Шлем"))
    assert park.general_count == 1


def test_duplicate_technics() -> None:
    inspector = FakeInspector(True)
    park = Park(inspector)
    park.success_technic(Bike("B1", "Велосипед", 7, True))

    with pytest.raises(ValueError, match="уже занят"):
        park.success_technic(Bike("B1", "Второй велосипед", 8, True))
    assert len(inspector.checked) == 1


def test_count() -> None:
    park = Park(FakeInspector(True))
    park.success_technic(Bike("B1", "Велосипед", 7, True))
    park.register_thing(Helmet("H1", "Шлем"))

    assert park.technic_count == 1
    assert park.thing_count == 1
    assert park.general_count == 2


def test_technics_beginner() -> None:
    park = Park(ServiceCenter())
    park.success_technic(Bike("B5", "Не для новичка", 5, True))
    park.success_technic(Bike("B6", "Для новичка", 6, True))
    park.success_technic(Bike("B9", "Сломан", 9, False))

    assert [x.inventory_number for x in park.technics_beginner()] == ["B6"]


def test_few_technic_thing() -> None:
    park = Park(ServiceCenter())
    park.success_technic(Samokat("S1", "Самокат", 8, True, 1.2))
    park.success_technic(Bike("B1", "Велосипед", 8, True))
    park.success_technic(Samokat("S2", "Сломанный", 9, False, 9.0))
    park.register_thing(ChargeWardrobe("C1", "Зарядный шкаф", 2.5))
    park.register_thing(Helmet("H1", "Шлем"))

    assert park.general_energy_use() == pytest.approx(3.7)


def test_park_empty() -> None:
    park = Park(FakeInspector(True))
    assert park.general_count == 0
    assert park.technics_beginner() == ()
    assert park.general_energy_use() == 0.0
