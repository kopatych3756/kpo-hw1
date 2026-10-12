from abc import ABC, abstractmethod


class IEnergyConsumer(ABC):

    @property
    @abstractmethod
    def energy_use(self) -> float:
        pass
