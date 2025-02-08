from abc import ABC, abstractmethod
from typing import Any

import numpy as np

from snake_env.memory_managers.memory_managers import MemoryManager
class Observator(ABC):
    @abstractmethod
    def get_observation(self):
        pass

class BasicObservator(Observator):
    def __init__(self, memory_manager: MemoryManager):
        super().__init__()
        self.memory_manager = memory_manager
        
    def get_observation(self):
        free_space = np.zeros((self.memory_manager['mapsize'][0], self.memory_manager['mapsize'][1], 3), dtype=np.uint8)
        snake_head_x, snake_head_y = self.memory_manager['snake_positions'][0]
        if snake_head_x == self.memory_manager['mapsize'][0]:
            snake_head_x = 0
        if snake_head_y == self.memory_manager['mapsize'][1]:
            snake_head_y = 0
        free_space[snake_head_x, snake_head_y] = [0, 255, 0]    
        for x, y in self.memory_manager['snake_positions'][1:]:
            if x == self.memory_manager['mapsize'][0]:
                x = 0
            if y == self.memory_manager['mapsize'][1]:
                y = 0
            free_space[x, y] = [0, 0, 255]
        for x, y in self.memory_manager['food_positions'] if self.memory_manager['food_positions'] else []:
            free_space[x, y] = [255, 0, 0]
        return free_space


class AbstractPositionalObservator(Observator):
    def __init__(self, memory_manager: MemoryManager):
        super().__init__()
        self.memory_manager = memory_manager
    def get_observation(self):
        free_space = np.zeros((self.memory_manager['mapsize'][0], self.memory_manager['mapsize'][1]), dtype=np.uint8)
        free_space[self.memory_manager['snake_positions'][0][0], self.memory_manager['snake_positions'][0][1]] = 1
        for x, y in self.memory_manager['snake_positions'][1:]:
            free_space[x, y] = 2
        for x, y in self.memory_manager['food_positions']:
            free_space[x, y] = 3
        return free_space   

class AdvancedObservator(Observator):
    pass