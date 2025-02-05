from abc import ABC, abstractmethod
from typing import Any

from snake_env.memory_managers.memory_managers import MemoryManager
class Observator(ABC):
    @abstractmethod
    def get_observation(self, data: MemoryManager):
        pass

class BasicObservator(Observator):
    pass


class AdvancedObservator(Observator):
    pass