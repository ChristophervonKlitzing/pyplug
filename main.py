from pyplug.plugin_loader import ModulePluginLoader
from pyplug.plugin_manager import PluginManager
from demo.demo_registries import DemoRegistry


if __name__ == "__main__":
    ploader = ModulePluginLoader("demo/demo_plugins/plugin_a")
    ploader.load()
    plugin = ploader.create_instance()
    
    manager = PluginManager()

    demo_registry = DemoRegistry()
    manager.add_registry(demo_registry)

    print(manager.get_registry_name_aliases())
    print(manager.get_registry_types())

    manager.add_plugin(ploader)