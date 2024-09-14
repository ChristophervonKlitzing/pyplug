from typing import Callable, TypeVar

from .object_registry import ObjectRegistry


class RegistryView:
    def __init__(self, class_getter: Callable[[type[ObjectRegistry]], ObjectRegistry], 
                 name_getter: Callable[[str], ObjectRegistry]) -> None:
        self._class_getter = class_getter
        self._name_getter = name_getter
    
    T = TypeVar('T', bound=ObjectRegistry)
    def get_registry_by_type(self, registry_type: type[T]) -> T:
        return self._class_getter(registry_type) # type: ignore
    
    def get_registry_by_name(self, registry_name: str) -> ObjectRegistry:
        return self._name_getter(registry_name)