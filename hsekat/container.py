from punq import Container
from .interfaces.IInspector import IInspector
from .services.ServiceCenter import ServiceCenter
from .Park import Park


def create_container() -> Container:
    container = Container()
    container.register(IInspector, ServiceCenter)
    container.register(Park)
    return container
