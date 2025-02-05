from abc import abstractmethod, ABC
from typing import Any
class MemoryManager(ABC):
    @abstractmethod
    def put(self, data):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def clear(self):
        pass
    
class BasicMemoryManager(MemoryManager):
    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value
        
    def __init__(self, **args: dict[str, Any]):
        pass
    
    def put(self, data):
        pass
    
    def get(self):
        pass    