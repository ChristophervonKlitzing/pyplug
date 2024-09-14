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