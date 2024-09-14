from pyplug.plugin_loader import ModulePluginLoader
from pyplug.plugin_registry_manager import PluginRegistryManager
from demo_files.demo_registries import DemoRegistry


if __name__ == "__main__":
    ploader = ModulePluginLoader("demo_files/test_plugins/plugin_a")
    ploader.load()
    
    # This will hold the registries and allow plugins to register to them.
    manager = PluginRegistryManager()

    # Add one demo registry for test purposes.
    demo_registry = DemoRegistry()
    manager.add_registry(demo_registry)

    # The registries can be accessed by their type or a name-alias (str).
    # To see what is available:
    print(manager.get_registry_name_aliases())
    print(manager.get_registry_types())
    print()

    # This will load the plugin and create an instance.
    # The instance can then register itself to any of the provided registries.
    plugin_id = manager.register_plugin(ploader.create_instance())
    manager.unregister_plugin(plugin_id)


    plugin_id = manager.register_plugin(ploader.create_instance())
    manager.unregister_plugin(plugin_id)
    
    # Instead also all plugins could be unregistered at once:
    # manager.unregister_all_plugins()