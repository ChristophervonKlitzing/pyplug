from pyplug.plugin import Plugin
from demo_files.demo_registries import DemoRegistry
from pyplug.registry_view import RegistryView

class MyPlugin(Plugin):
    def register(self, registry_view: RegistryView):
        registry_view.get_registry_by_type(DemoRegistry).register_plugin(self)
