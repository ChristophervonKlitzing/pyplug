from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .plugin import Plugin


class ObjectRegistry(ABC):
    @abstractmethod
    def register_plugin(self, plugin: 'Plugin'):
        raise NotImplementedError