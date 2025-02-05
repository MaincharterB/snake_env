from abc import ABC, abstractmethod
import cv2
import numpy as np
from snake_env.observators.observators import Observator
class Renderer(ABC):
    @abstractmethod
    def render(self):
        pass

class HumanRenderer(Renderer):
    def __init__(self, observator: Observator):
        super().__init__()
        self.observator = observator
    def render(self):
        observation = self.observator.get_observation()
        return observation


class RGBArrayRenderer(Renderer):
    def __init__(self, observator: Observator):
        super().__init__()
        self.observator = observator
    def render(self):
        observation = self.observator.get_observation()
        
        return observation