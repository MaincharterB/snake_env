from snake_env.envs.env import SimpleSnakeEnv
from snake_env.utils.configs import BaseConfig


def BasicEnv36x36():
    snake_config = BaseConfig(36, 36, render_mode='rgb_array', init_snake_size=6)
    return SimpleSnakeEnv(**vars(snake_config))