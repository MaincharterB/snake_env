from abc import ABC, abstractmethod

from snake_env.utils.configs import FoodConfig
class FoodPlacer(ABC):
    @abstractmethod
    def place_food(self, observation):
        pass

class RandomFoodPlacer(FoodPlacer):
    def __init__(self, **args: FoodConfig):
        pass
    pass

class NearFoodPlacer(FoodPlacer):
    pass