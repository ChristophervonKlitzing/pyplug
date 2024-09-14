from abc import ABC

from .plugin_loader import PluginLoader
from .object_registry import ObjectRegistry
from .registry_state import RegistryState
from .plugin import Plugin
from .types import RegistryId


class PluginRegistryManager(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._next_id: RegistryId = 0
        self._registries_by_type: dict[type[ObjectRegistry], ObjectRegistry] = {}
        self._registries_by_name: dict[str, ObjectRegistry] = {}

        self._registry_states: dict[RegistryId, RegistryState] = {}
    
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
    
    def register_plugin(self, plugin: 'Plugin'):
        plugin_id = self._create_next_id()
        registry_view = RegistryState(self._registries_by_type.__getitem__, self._registries_by_name.__getitem__)
        plugin.register(registry_view)
        self._registry_states[plugin_id] = registry_view
        return plugin_id
    
    def unregister_plugin(self, plugin_id: RegistryId):
        registry_view = self._registry_states.pop(plugin_id)
        registry_view.cleanup()
    
    def unregister_all_plugins(self):
        for plugin_id in set(self._registry_states.keys()): # copy because elements removed during iteration
            self.unregister_plugin(plugin_id)