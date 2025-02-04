from dataclasses import dataclass
from typing import Literal

@dataclass
class FoodConfig:
    num_placed_foods_per_episode: int = 1
    food_place_strategy: Literal["random", "near"] = "random"
    food_size: int = 1

@dataclass
class RewardConfig:
    food_reward: float = 1.0
    collision_reward: float = -1.0
    time_reward: float = 0.0
    near_food_reward: float = 0.0
    
@dataclass
class BaseConfig:
    height: int
    width: int
    max_steps: int = 1000
    use_time_limit: bool = True
    render_mode: Literal["human", "rgb_array"] = "rgb_array"
    food_config: FoodConfig = FoodConfig()
    reward_config: RewardConfig = RewardConfig()