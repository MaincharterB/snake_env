from snake_env.envs.env import SimpleSnakeEnv
from snake_env.utils.configs import BaseConfig, FoodConfig

# Basic Env
def BasicEnv36x36():
    snake_config = BaseConfig(36, 36, render_mode='rgb_array', init_snake_size=6)
    return SimpleSnakeEnv(**vars(snake_config))

def BasicEnv48x48():
    snake_config = BaseConfig(48, 48, render_mode='rgb_array', init_snake_size=6)
    return SimpleSnakeEnv(**vars(snake_config))
def BasicEnv64x64():
    snake_config = BaseConfig(64, 64, render_mode='rgb_array', init_snake_size=6)
    return SimpleSnakeEnv(**vars(snake_config))

# Near Env
def NearEnv36x36():
    food_confid = FoodConfig(num_placed_foods_per_episode=1, food_place_strategy='near', food_size=1)
    snake_config = BaseConfig(36, 36, render_mode='rgb_array', init_snake_size=6, food_config=food_confid)
    return SimpleSnakeEnv(**vars(snake_config))

def NearEnv48x48():
    food_confid = FoodConfig(num_placed_foods_per_episode=1, food_place_strategy='near', food_size=1)
    snake_config = BaseConfig(48, 48, render_mode='rgb_array', init_snake_size=6, food_config=food_confid)
    return SimpleSnakeEnv(**vars(snake_config))

def NearEnv64x64():
    food_confid = FoodConfig(num_placed_foods_per_episode=1, food_place_strategy='near', food_size=1)
    snake_config = BaseConfig(64, 64, render_mode='rgb_array', init_snake_size=6, food_config=food_confid)
    return SimpleSnakeEnv(**vars(snake_config))