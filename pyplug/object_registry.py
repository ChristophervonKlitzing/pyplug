from typing import TypeVar, Protocol

from .types import ResourceId



T = TypeVar('T', contravariant=True)
class ObjectRegistry(Protocol[T]):
    def register_object(self, __obj: T) -> ResourceId | None:
        ...
    
    def clean_resource(self, __resource_id: ResourceId):
        ...