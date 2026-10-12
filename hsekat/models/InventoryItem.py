from ..interfaces.IInventoryItem import IInventoryItem


class InventoryItem(IInventoryItem):
    def __init__(self, inventory_number: str, name: str):
        if not isinstance(inventory_number, str) or not inventory_number.strip():
            raise ValueError("Инвентарный номер должен быть непустой строкой")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Наименование должно быть непустой строкой")
        self._inventory_number = inventory_number
        self._name = name

    @property
    def inventory_number(self) -> str:
        return self._inventory_number

    @property
    def name(self) -> str:
        return self._name
