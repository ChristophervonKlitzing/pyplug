from abc import ABC

from .object_registry import ObjectRegistry
from .object_registry_state import ObjectRegistryState
from .registrable import Registrable
from .types import RegistryId


class RegistryScope:
    def __init__(self, obj: Registrable, manager: 'ObjectRegistryManager') -> None:
        self._obj = obj
        self._manager = manager
        self._reg_id: RegistryId | None = None
    
    def __enter__(self):
        self._reg_id = self._manager.register_object(self._obj)
        return self._reg_id
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        if self._reg_id is not None:
            self._manager.unregister_object(self._reg_id)

class ObjectRegistryManager(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._next_id: RegistryId = 0
        self._registries_by_type: dict[type[ObjectRegistry], ObjectRegistry] = {}
        self._registries_by_name: dict[str, ObjectRegistry] = {}

        self._registry_states: dict[RegistryId, ObjectRegistryState] = {}
    
    def _create_next_id(self) -> RegistryId:
        id = self._next_id
        self._next_id += 1
        return id 
    
    def add_registry(self, registry: ObjectRegistry, names: set[str] | None = None, default_class_name: bool = True):
        self._registries_by_type[type(registry)] = registry

        if names is not None:
            for name in names:
                self.bind_registry_name(type(registry), name)
        
        if default_class_name:
            self.bind_registry_name(type(registry), type(registry).__name__)
    
    def bind_registry_name(self, registry_type: type[ObjectRegistry], name: str):
        self._registries_by_name[name] = self._registries_by_type[registry_type]
    
    def get_registry_name_aliases(self):
        return set(self._registries_by_name.keys())
    
    def get_registry_types(self):
        return set(self._registries_by_type.keys())
    
    def register_object(self, obj: Registrable):
        obj_id = self._create_next_id()
        registry_view = ObjectRegistryState(self._registries_by_type.__getitem__, self._registries_by_name.__getitem__)
        obj.register(registry_view)
        self._registry_states[obj_id] = registry_view
        return obj_id
    
    def unregister_object(self, obj_id: RegistryId):
        registry_view = self._registry_states.pop(obj_id)
        registry_view.cleanup()

    def register_scoped(self, obj: Registrable) -> RegistryScope:
        return RegistryScope(obj, self)
    
    def unregister_all_objects(self):
        for obj_id in set(self._registry_states.keys()): # copy because elements removed during iteration
            self.unregister_object(obj_id)