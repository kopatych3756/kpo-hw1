from abc import ABC, abstractmethod


class IInventoryItem(ABC):
    
    @property
    @abstractmethod
    def inventory_number(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass
