from pyplug.plugin_loader import ModulePluginLoader
from pyplug.plugin_manager import PluginManager
from demo_files.demo_registries import DemoRegistry


if __name__ == "__main__":
    ploader = ModulePluginLoader("demo_files/test_plugins/plugin_a")
    
    # This will hold the registries and allow plugins to register to them.
    manager = PluginManager()

    # Add one demo registry for test purposes.
    demo_registry = DemoRegistry()
    manager.add_registry(demo_registry)

    # The registries can be accessed by their type or a name-alias (str).
    # To see what is available:
    print(manager.get_registry_name_aliases())
    print(manager.get_registry_types())

    # This will load the plugin and create an instance.
    # The instance can then register itself to any of the provided registries.
    manager.add_plugin_loader(ploader)

    # The plugin could also directly be added using:
    # ploader.load()
    # plugin = ploader.create_instance()
    # manager.add_plugin(plugin)