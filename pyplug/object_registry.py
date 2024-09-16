from typing import TypeVar, Generic
from abc import ABC, abstractmethod

from .types import ResourceId



T = TypeVar('T', contravariant=True)
class ObjectRegistry(ABC, Generic[T]):
    @abstractmethod
    def register_object(self, __obj: T) -> ResourceId | None:
        raise NotImplementedError
    
    @abstractmethod
    def clean_resource(self, __resource_id: ResourceId):
        raise NotImplementedError