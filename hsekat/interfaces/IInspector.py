from abc import ABC, abstractmethod
from ..models.Technic import Technic


class IInspector(ABC):

    @abstractmethod
    def check(self, technic: Technic) -> bool:
        pass
