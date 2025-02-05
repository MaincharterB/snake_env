from abc import abstractmethod, ABC
from typing import Any

from snake_env.enums.actions import Direction, Status
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
        super(BasicMemoryManager, self).__init__()
        self.snake_positions = []
        self.food_positions = []
        self.direction = None
        self.mapsize = [args['width'], args['height']]
        self.status = Status.ALIVE
        self.args = args
        
    def put(self, key, value):
        self[key] = value
    
    def get(self, key):
        return self[key]
    
    def clear(self):
        self.snake_positions = []
        self.food_positions = []
        self.direction = None
        self.status = Status.ALIVE