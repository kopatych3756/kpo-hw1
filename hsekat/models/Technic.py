from ..interfaces.IEnergyConsumer import IEnergyConsumer
from .InventoryItem import InventoryItem
from ._validation import validate_energy


class Technic(InventoryItem):
    def __init__(self, inventory_number: str, name: str, ease: int, is_check: bool):
        super().__init__(inventory_number, name)
        if type(ease) is not int or not(1 <= ease <= 10):
            raise ValueError("Простота должна быть целым числом от 1 до 10")
        if type(is_check) is not bool:
            raise ValueError("Состояние должно быть True или False")
        self._ease = ease
        self._is_check = is_check

    @property
    def ease(self) -> int:
        return self._ease

    @property
    def is_check(self) -> bool:
        return self._is_check


class ElectricTechnic(Technic, IEnergyConsumer):
    def __init__(self, inventory_number: str, name: str, ease: int, is_check: bool, energy_use: float):
        super().__init__(inventory_number, name, ease, is_check)
        self._energy_use = validate_energy(energy_use)

    @property
    def energy_use(self) -> float:
        return self._energy_use


class Bike(Technic):
    pass


class Samokat(ElectricTechnic):
    pass


class ElectricBike(ElectricTechnic):
    pass
