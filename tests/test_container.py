from hsekat.container import create_container
from hsekat.Park import Park
from hsekat.models.Technic import Bike


def test_container():
    container = create_container()
    park = container.resolve(Park)
    bike = Bike("B1", "Велосипед", 7, True)

    assert park.success_technic(bike) is True
    assert park.technic_count == 1
