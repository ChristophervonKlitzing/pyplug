from abc import ABC, abstractmethod
import os
from importlib import util
import sys
import inspect

from .plugin import Plugin


class PluginLoader(ABC):
    @abstractmethod
    def load(self):
        raise NotImplementedError
    
    @abstractmethod
    def unload(self):
        raise NotImplementedError

    @abstractmethod
    def is_loaded(self) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def create_instance(self) -> Plugin:
        raise NotImplementedError
    



class ModulePluginLoader(PluginLoader):
    def __init__(self, directory_path: str, module_name: str = "__init__.py") -> None:
        super().__init__()
        self._directory_path = directory_path 
        self._module_name = module_name
        self._module_path = os.path.join(self._directory_path, self._module_name)
        self._plugin_name = self._directory_path.replace(".", "_")

        self._module = None

    def load(self):
        if self.is_loaded():
            return 

        if not os.path.exists(self._module_path):
            raise RuntimeError(f"Module '{self._module_path}' is not existing")

        if self._plugin_name not in sys.modules:
            # Create the module spec
            spec = util.spec_from_file_location(self._plugin_name, self._module_path, submodule_search_locations=[])

            # Create a new module based on the spec
            module = util.module_from_spec(spec)

            # Set __package__ to ensure relative imports work
            module.__package__ = self._plugin_name

            # Load the module by executing it
            sys.modules[self._plugin_name] = module
            spec.loader.exec_module(module)
        else:
            module = sys.modules[self._plugin_name]

        self._module = module

    def unload(self):
        self._module = None

    def is_loaded(self) -> bool:
        return self._module is not None
    
    def _get_plugin_classes(self) -> list[type[Plugin]]:
        """Retrieve all subclasses of `Plugin` from the loaded module."""

        if self._module is None:
            raise RuntimeError("Module not loaded")

        # Use inspect to get all classes defined in the module
        plugin_classes = []
        for _, obj in inspect.getmembers(self._module, inspect.isclass):
            if issubclass(obj, Plugin) and obj is not Plugin:
                plugin_classes.append(obj)
        return plugin_classes

    def create_instance(self) -> Plugin:
        if not self.is_loaded():
            raise RuntimeError("Can not create plugin instance of plugin is not loaded")
        
        potential_classes = self._get_plugin_classes()
        num_classes = len(potential_classes)

        if num_classes == 0:
            raise RuntimeError(f"Could not find any sub-class of class '{Plugin.__name__}' in plugin '{self._plugin_name}'")
        elif num_classes > 1:
            class_names = [cls.__name__ for cls in potential_classes]
            raise RuntimeError(f"Only one sub-class of class '{Plugin.__name__}' allowed in plugin '{self._plugin_name}' but found {num_classes}: {class_names}")
        
        return potential_classes[0]()
