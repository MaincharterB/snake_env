from abc import ABC, abstractmethod
class Renderer(ABC):
    @abstractmethod
    def render(self, observation):
        pass

class HumanRenderer(Renderer):
    pass


class RGBArrayRenderer(Renderer):
    pass