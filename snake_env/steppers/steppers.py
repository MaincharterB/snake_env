from abc import ABC, abstractmethod
from typing import Any, SupportsFloat

import numpy as np

from snake_env.enums.actions import Direction, Status
from snake_env.food_placers.food_placers import FoodPlacer
from snake_env.memory_managers.memory_managers import MemoryManager
class Stepper(ABC):
    @abstractmethod
    def step(self, action):
        pass
    
class BasicStepper(Stepper):
    def __init__(self, food_placer: FoodPlacer, memory_manager: MemoryManager):
        super().__init__()
        self.food_placer = food_placer 
        self.memory_manager = memory_manager
    
    def is_border_collided(self):
        snake_position = self.memory_manager['snake_positions']
        w, h = self.memory_manager['mapsize']
        snake_head_position = snake_position[0]
        x, y = snake_head_position
        return x < 0 or x > w-1 or y < 0 or y > h-1
    
    def is_self_collided(self):
        snake_position = self.memory_manager['snake_positions']
        for i in range(1, len(snake_position)):
            if np.array_equal(snake_position[0], snake_position[i]):
                return True
        return False
    
    def is_food_collided(self):
        snake_position = self.memory_manager['snake_positions']
        food_position = self.memory_manager['food_positions']
        for food_id in range(len(food_position)):
            if np.array_equal(snake_position[0], food_position[food_id]):
                del food_position[food_id]
                self.memory_manager['food_positions'] = food_position
                return True
        return False
    
    def get_status(self):
        if self.is_border_collided() or self.is_self_collided():
            return Status.DEAD
        if self.is_food_collided():
            return Status.EAT_FOOD
        return Status.ALIVE
    
    def sum_positions(self, position, direction):
        return position[0] + direction[0], position[1] + direction[1]
    
    
    def get_new_position(self, action):
        action = list(Direction)[action]
        snake_position = self.memory_manager['snake_positions']
        snake_head_position = snake_position[0]
        direction: Direction = self.memory_manager['direction']
        new_head_position = snake_head_position
        if action == direction.opposite:
            new_head_position = self.sum_positions(new_head_position, direction.value)
        else:
            new_head_position = self.sum_positions(new_head_position, action.value)
            direction = action
        self.memory_manager['direction'] = direction   
        snake_position.insert(0, new_head_position) 
        del snake_position[-1]
        return snake_position
    def add_new_tail(self):
        last_tail_position = self.memory_manager['snake_positions'][-1]
        pre_last_tail_position = self.memory_manager['snake_positions'][-2]
        tail_direction = (last_tail_position[0] - pre_last_tail_position[0], last_tail_position[1] - pre_last_tail_position[1])
        added_tail_position = self.sum_positions(last_tail_position, tail_direction)
        self.memory_manager['snake_positions'].append(added_tail_position)    
        
    def step(self, action):
        self.memory_manager['snake_positions']  = self.get_new_position(action)  
        new_status = self.get_status()
        self.memory_manager['status'] = new_status
        if new_status == Status.EAT_FOOD:
            self.add_new_tail()
            self.food_placer.place_food()
        
            
    
class AdvancedStepper(Stepper):
    def step(self, action):
        pass    