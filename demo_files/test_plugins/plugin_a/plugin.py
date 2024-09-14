from pyplug.plugin import Plugin
from demo_files.demo_registries import DemoRegistry
from pyplug.registry_state import RegistryState

class MyPlugin(Plugin):
    def register(self, registry_state: RegistryState):
        registry_state.register_by_type(DemoRegistry, self)
