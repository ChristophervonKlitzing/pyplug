from abc import ABC, abstractmethod

from pyplug.registry_state import ObjectRegistryState


class Registrable(ABC):
    @abstractmethod
    def register(self, registry_state: ObjectRegistryState):
        raise NotImplementedError