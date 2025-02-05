from enum import Enum
 
class Direction(Enum):
    UP = [-1, 0]
    RIGHT = [0, 1]
    DOWN = [1, 0]
    LEFT = [0, -1]
    
    @property
    def opposite(self):
      direction_list = list(Direction)  
      curr_ind = direction_list.index(self)
      return direction_list[(curr_ind + 2) % len(direction_list)]
  
class Status(Enum):
    ALIVE = 0
    EAT_FOOD = 1
    DEAD = 2  