

import numpy as np
from snake_env.memory_managers.memory_managers import MemoryManager
from snake_env.utils.configs import FoodConfig
from itertools import product
class FoodPlacer():
    def __init__(self, memory_manager: MemoryManager,**args: FoodConfig):
        self.memory_manager = memory_manager
        self.args = args
        
    def get_free_space(self):
        w, h = self.memory_manager['mapsize']
        map_all = list(product(range(w), range(h)))  
        map_free = list(set(map_all) - set(self.memory_manager['snake_positions']) - set(self.memory_manager['food_positions']))
        return map_free
   
    def get_required_count(self):
        req_free_space = self.args['num_placed_foods_per_episode']
        req_free_space = abs(len(self.memory_manager['food_positions']) - req_free_space)
        return req_free_space
            
    def random_place(self):
        food_positions:list = self.memory_manager["food_positions"]
        req_free_space = self.get_required_count()
        # TODO implement for different sizes (default is 1)
        free_space = self.get_free_space()
        for _ in range(req_free_space):
            while True:
                x = np.random.randint(0, self.memory_manager['mapsize'][0])
                y = np.random.randint(0, self.memory_manager['mapsize'][1])
                if (x, y) in free_space:
                    food_positions.append((x, y))
                    break      
                
        self.memory_manager["food_positions"] = food_positions   

    def near_place(self):
        food_positions:list = self.memory_manager["food_positions"]
        req_free_space = self.get_required_count()
        # TODO implement for different sizes (default is 1)
        free_space = self.get_free_space()
        for _ in range(req_free_space):
            while True:
                x = np.random.randint(0, self.memory_manager['mapsize'][0])
                y = np.random.randint(0, self.memory_manager['mapsize'][1])
                if (x, y) in free_space and abs(x - self.memory_manager['snake_positions'][0][0]) < 2 and abs(y - self.memory_manager['snake_positions'][0][1]) < 2:
                    food_positions.append((x, y))
                    break
        self.memory_manager["food_positions"] = food_positions
    
    def place_food(self):
        strategy: str = self.args['food_place_strategy']
        if strategy == 'random':
            self.random_place()
        elif strategy == 'near':
            self.near_place()
        
