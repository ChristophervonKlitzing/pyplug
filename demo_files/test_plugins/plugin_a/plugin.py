from pyplug.plugin import Plugin
from demo_files.demo_registries import DemoRegistry
from pyplug.registry.object_registry_state import ObjectRegistryState


class MyPlugin(Plugin):
    def register(self, registry_state: ObjectRegistryState):
        registry_state.register_by_type(DemoRegistry, self)
