from pyplug.object_registry import ObjectRegistry
from pyplug.plugin import Plugin
from pyplug.types import ResourceId


class DemoRegistry(ObjectRegistry[Plugin]):
    _next_id = 0

    def __init__(self) -> None:
        self._resource_ids = set()

    def register_object(self, p: Plugin):
        id = DemoRegistry._next_id
        DemoRegistry._next_id += 1
        print("Register plugin to demo-registry", p)
        self._resource_ids.add(id)
        return id
    
    def clean_resource(self, resource_id: ResourceId):
        print("Cleanup resource", resource_id)
        self._resource_ids.remove(resource_id)














    