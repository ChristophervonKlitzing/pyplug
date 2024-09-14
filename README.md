# Python Plugin Registry
Small python library for loading and managing versatile python plugins. 
It allows plugins to self-register to a registry-system.
A flexible interface allows different kind of 
plugins (python modules, remote services, ...) to be loaded.

## Applications
This library might be useful if a plugin can have multiple functionalities 
like adding a GUI-component, adding settings and providing a service for processing.
In this case, it can decide itself, what its abilities are. It can register itself
in a typed way to the according registries.

## Missing but possible
### Add/remove plugins
- The plugin-manager could hold the plugin-instances and return an id for each added plugin.
- Plugins can be removed by id (potential for automatic cleanup)

## Automatic cleanup
When a plugin gets removed, all acquired resources in the registries, could be automatically cleaned.
A plugin might not register itself but objects it created. These objects must be linked to the plugin on registry.
If this linkage information is available, all resources, connected to that plugin, could be automatically removed.