from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyplug.registry_state import RegistryState


class Plugin(ABC):
    @abstractmethod
    def register(self, registry_state: 'RegistryState'):
        raise NotImplementedError
    
    