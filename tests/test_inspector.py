import pytest
from hsekat.models.Technic import Bike
from hsekat.services.ServiceCenter import ServiceCenter


@pytest.mark.parametrize("is_check", [True, False])
def test_inspector(is_check: bool) -> None:
    bike = Bike("B1", "Велосипед", 7, is_check)
    assert ServiceCenter().check(bike) is is_check
