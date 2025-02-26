from dataclasses import dataclass, field
from typing import Literal

from snake_env.enums.path_linkers import PathLinkDirection

@dataclass
class FoodConfig:
    num_placed_foods_per_episode: int = 1
    food_place_strategy: Literal["random", "near"] = "random"
    food_size: int | list[int] = 1

@dataclass
class RewardConfig:
    food_reward: float = 1.0
    collision_reward: float = -1.0
    time_reward: float = 0.0
    near_food_reward: float = 0.0
    
@dataclass
class LinkConfig:
    link_from: int
    height: int
    width: int
    link_direction: PathLinkDirection = PathLinkDirection.TOP           
@dataclass
class BaseConfig:
    height: int
    width: int
    linked_paths: list[LinkConfig] = field(default_factory=list)
    init_snake_size: int = 3
    max_steps: int = 1000
    use_time_limit: bool = True
    render_mode: Literal["human", "rgb_array"] = "rgb_array"
    food_config: FoodConfig = field(default_factory=FoodConfig)
    reward_config: RewardConfig = field(default_factory=RewardConfig)
    
