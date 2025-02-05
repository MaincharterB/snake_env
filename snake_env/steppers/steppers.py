from abc import ABC, abstractmethod
from typing import Any, SupportsFloat

from snake_env.memory_managers.memory_managers import MemoryManager
class Stepper(ABC):
    @abstractmethod
    def step(self, action, data: MemoryManager) -> tuple[Any, SupportsFloat, bool, bool, dict[str, Any]]:
        pass
    
class BasicStepper(Stepper):
    def step(self, action, data: dict[str, Any]):
        pass    
    
class AdvancedStepper(Stepper):
    def step(self, action, data: dict[str, Any]):
        pass    