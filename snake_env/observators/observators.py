from abc import ABC, abstractmethod
from typing import Any

import numpy as np

from snake_env.enums.path_linkers import PathLinkDirection
from snake_env.memory_managers.memory_managers import MemoryManager
from snake_env.utils.configs import LinkConfig
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

class ComplexPositionalObservator(AbstractPositionalObservator):
    def __init__(self, memory_manager: MemoryManager):
        super().__init__(memory_manager)
        self.memory_manager = memory_manager
        self.empty_color = [0, 0, 0]
        self.place_color = [255, 255, 255]
        self.snake_head_color = [0, 255, 0]
        self.snake_body_color = [0, 0, 255]
        self.food_color = [255, 0, 0]
    
    def _process_space(self, space: LinkConfig):
        x, y = space.width, space.height
        offset = space.link_from
        if space.link_direction == PathLinkDirection.TOP or space.link_direction == PathLinkDirection.BOTTOM:
            y+= offset
        if space.link_direction == PathLinkDirection.LEFT or space.link_direction == PathLinkDirection.RIGHT:
            x+= offset
        return x, y            
    
    def _get_full_space(self, memory_manager: MemoryManager):
        full_places = [[memory_manager['mapsize'][0], memory_manager['mapsize'][1]]]
        for space in memory_manager["linked_spaces"]:
            space:LinkConfig = space
            x, y = self._process_space(space)
            full_places.append((x, y))
        max_x, max_y = max(full_places, key=lambda x: x[0])[0], max(full_places, key=lambda x: x[1])[1]
        return np.zeros((max_x+1, max_y+1, 3), dtype=np.uint8)
            
    def get_observation(self):
        space = self._get_full_space(self.memory_manager)
        free_space = super().get_observation()
        free_space = np.expand_dims(free_space, axis=2)
        return free_space

class AdvancedObservator(Observator):
    pass