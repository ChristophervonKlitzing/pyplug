from abc import ABC, abstractmethod

from pyplug.registry_state import RegistryState


class Plugin(ABC):
    @abstractmethod
    def register(self, registry_state: 'RegistryState'):
        raise NotImplementedError
    
    