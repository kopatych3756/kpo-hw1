from ..interfaces.IEnergyConsumer import IEnergyConsumer
from .InventoryItem import InventoryItem
from ._validation import validate_energy


class Thing(InventoryItem):
    pass


class ThingPowered(Thing, IEnergyConsumer):
    def __init__(self, inventory_number: str, name: str, energy_use: float):
        super().__init__(inventory_number, name)
        self._energy_use = validate_energy(energy_use)

    @property
    def energy_use(self) -> float:
        return self._energy_use


class Helmet(Thing):
    pass


class DockStation(ThingPowered):
    pass


class ChargeWardrobe(ThingPowered):
    pass
