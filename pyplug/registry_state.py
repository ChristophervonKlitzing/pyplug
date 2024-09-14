from collections import defaultdict
from typing import Callable, TypeVar

from .object_registry import ObjectRegistry
from .types import ResourceId


class RegistryState:
    def __init__(self, class_getter: Callable[[type[ObjectRegistry]], ObjectRegistry], 
                 name_getter: Callable[[str], ObjectRegistry]) -> None:
        self._class_getter = class_getter
        self._name_getter = name_getter

        self._aquired_resources: dict[type[ObjectRegistry], set[ResourceId]] = defaultdict(set)
    
    T = TypeVar('T')
    def __get_registry_by_type(self, registry_type: type[ObjectRegistry[T]]) -> ObjectRegistry[T]:
        return self._class_getter(registry_type)
    
    T = TypeVar('T')
    def register_by_type(self, registry_type: type[ObjectRegistry[T]], plugin: T):
        registry = self.__get_registry_by_type(registry_type)
        resource_id = registry.register_object(plugin)

        if resource_id is not None:
            self._aquired_resources[registry_type].add(resource_id)
    
    def cleanup(self):
        for registry_type, resource_ids in self._aquired_resources.items():
            registry = self.__get_registry_by_type(registry_type)
            for rid in resource_ids:
                registry.clean_resource(rid)
        self._aquired_resources.clear()