from abc import ABC, abstractmethod
from typing import Any, SupportsFloat
class Stepper(ABC):
    @abstractmethod
    def step(self, action, data: dict[str, Any]) -> tuple[Any, SupportsFloat, bool, bool, dict[str, Any]]:
        pass
    
class BasicStepper(Stepper):
    def step(self, action, data: dict[str, Any]):
        pass    
    
class AdvancedStepper(Stepper):
    def step(self, action, data: dict[str, Any]):
        pass    