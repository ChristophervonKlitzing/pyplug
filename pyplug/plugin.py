from abc import ABC, abstractmethod

from pyplug.registry_view import RegistryView


class Plugin(ABC):
    @abstractmethod
    def register(self, registry_view: 'RegistryView'):
        raise NotImplementedError
    
    