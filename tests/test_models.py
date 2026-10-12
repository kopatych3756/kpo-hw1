import pytest
from hsekat.interfaces.IEnergyConsumer import IEnergyConsumer
from hsekat.interfaces.IInventoryItem import IInventoryItem
from hsekat.models.Technic import *
from hsekat.models.Thing import *


def test_inventory() -> None:
    helmet = Helmet("H1", "Шлем")
    assert isinstance(helmet, IInventoryItem)
    assert helmet.inventory_number == "H1"
    assert helmet.name == "Шлем"
    assert not isinstance(helmet, IEnergyConsumer)


def test_electric_items() -> None:
    samokat = Samokat("S1", "Самокат", 7, True, 1.5)
    chargewardrobe = ChargeWardrobe("C1", "Шкаф", 2.5)
    assert isinstance(samokat, IEnergyConsumer)
    assert isinstance(chargewardrobe, IEnergyConsumer)
    assert samokat.energy_use == 1.5
    assert chargewardrobe.energy_use == 2.5


@pytest.mark.parametrize("number, name", [("", "Шлем"), (" ", "Шлем"), ("H1", ""), ("H1", " "), (None, "Шлем"), ("H1", 3)])
def test_invalid_inventory_number(number, name) -> None:
    with pytest.raises(ValueError):
        Helmet(number, name)


@pytest.mark.parametrize("ease", [0, 11, 2.5, True, "6"])
def test_invalid_ease(ease) -> None:
    with pytest.raises(ValueError):
        Bike("B1", "Велосипед", ease, True)


@pytest.mark.parametrize("is_check", [1, None, "yes"])
def test_invalid_technic_check(is_check) -> None:
    with pytest.raises(ValueError):
        Bike("B1", "Велосипед", 6, is_check)


@pytest.mark.parametrize("energy", [-1, True, "1.2", None])
@pytest.mark.parametrize("factory", [lambda energy: Samokat("S1", "Самокат", 6, True, energy), lambda energy: ChargeWardrobe("C1", "Зарядный шкаф", energy)])
def test_invalid_energy(factory, energy) -> None:
    with pytest.raises(ValueError):
        factory(energy)


def test_inventory_number_change() -> None:
    helmet = Helmet("H1", "Шлем")
    with pytest.raises(AttributeError):
        helmet.inventory_number = "ERROR"
