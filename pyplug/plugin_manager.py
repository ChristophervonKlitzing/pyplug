from abc import ABC

from .plugin_loader import PluginLoader
from .object_registry import ObjectRegistry
from .registry_view import RegistryView


class PluginManager(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._registries_by_type: dict[type[ObjectRegistry], ObjectRegistry] = {}
        self._registries_by_name: dict[str, ObjectRegistry] = {}
    
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
    
    def add_plugin(self, plugin_loader: PluginLoader):
        if not plugin_loader.is_loaded():
            plugin_loader.load()
        
        plugin = plugin_loader.create_instance()
        plugin.register(RegistryView(self._registries_by_type.__getitem__, self._registries_by_name.__getitem__))