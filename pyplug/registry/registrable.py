from abc import ABC, abstractmethod

from .object_registry_state import ObjectRegistryState


class Registrable(ABC):
    @abstractmethod
    def register(self, registry_state: ObjectRegistryState):
        raise NotImplementedError