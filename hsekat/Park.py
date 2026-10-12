from .interfaces.IInspector import IInspector
from .interfaces.IEnergyConsumer import IEnergyConsumer
from .models.Technic import Technic
from .models.Thing import Thing


class Park:
    def __init__(self, inspector: IInspector):
        self._inspector = inspector
        self._technics: dict[str, Technic] = dict()
        self._things: dict[str, Thing] = dict()

    def _check_free_number(self, number: str) -> None:
        if number in self._technics or number in self._things:
            raise ValueError(f"Инвентарный номер {number} уже занят")

    def success_technic(self, technic: Technic) -> bool:
        self._check_free_number(technic.inventory_number)
        if not self._inspector.check(technic):
            return False
        self._technics[technic.inventory_number] = technic
        return True

    def register_thing(self, thing: Thing) -> None:
        self._check_free_number(thing.inventory_number)
        self._things[thing.inventory_number] = thing

    @property
    def technic_count(self) -> int:
        return len(self._technics)

    @property
    def thing_count(self) -> int:
        return len(self._things)

    @property
    def general_count(self) -> int:
        return self.technic_count + self.thing_count

    def technics(self):
        return tuple(self._technics.values())

    def all_inventory(self):
        return (*self._technics.values(), *self._things.values())

    def technics_beginner(self):
        return tuple(technic for technic in self._technics.values() if technic.ease >= 6)

    def general_energy_use(self) -> float:
        return sum(item.energy_use for item in self.all_inventory() if isinstance(item, IEnergyConsumer))
        

    
