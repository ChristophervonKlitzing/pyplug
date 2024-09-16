from pyplug.plugin_loader import ModulePluginLoader
from pyplug.object_registry_manager import ObjectRegistryManager
from demo_files.demo_registries import DemoRegistry


if __name__ == "__main__":
    ploader = ModulePluginLoader("demo_files/test_plugins/plugin_a")
    ploader.load()
    
    # This will hold the registries and allow plugins to register to them.
    manager = ObjectRegistryManager()

    # Add one demo registry for test purposes.
    demo_registry = DemoRegistry()
    manager.add_registry(demo_registry)

    # The registries can be accessed by their type or a name-alias (str).
    # To see what is available:
    print(manager.get_registry_name_aliases())
    print(manager.get_registry_types())
    print()

    # The instance can then register itself to any of the provided registries.
    reg_id = manager.register_object(ploader.create_instance())
    manager.unregister_object(reg_id)


    reg_id = manager.register_object(ploader.create_instance())
    manager.unregister_object(reg_id)

    # A scoped registry:
    obj = ploader.create_instance()
    with manager.register_scoped(obj) as reg_id:
        print("registry-id", reg_id)
    
    # Instead also all objects could be unregistered at once:
    # manager.unregister_all_objects()