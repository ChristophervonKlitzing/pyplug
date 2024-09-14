from pyplug.object_registry import ObjectRegistry
from pyplug.plugin import Plugin


class DemoRegistry(ObjectRegistry):
    def register_plugin(self, plugin: Plugin):
        print("Register plugin to demo-registry", plugin)
    