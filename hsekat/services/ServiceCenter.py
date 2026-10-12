from ..interfaces.IInspector import IInspector
from ..models.Technic import Technic


class ServiceCenter(IInspector):
    def check(self, technic: Technic) -> bool:
        return technic.is_check
