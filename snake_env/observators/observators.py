from abc import ABC, abstractmethod
from typing import Any
class Observator(ABC):
    @abstractmethod
    def get_observation(self, data: dict[str, Any]):
        pass

class BasicObservator(Observator):
    pass


class AdvancedObservator(Observator):
    pass