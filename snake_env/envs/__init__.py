from .env import SimpleSnakeEnv
from .factory import BasicEnv36x36, BasicEnv48x48, BasicEnv64x64, NearEnv36x36, NearEnv48x48, NearEnv64x64
from gymnasium.envs.registration import register

__all__ = ["SimpleSnakeEnv", "BasicEnv36x36", "BasicEnv48x48", "BasicEnv64x64", "NearEnv36x36", "NearEnv48x48", "NearEnv64x64"]

# Basic Envs
register(
    id="Simple-Snake-36x36-v0",
    entry_point="snake_env.envs.factory:BasicEnv36x36",
)

register(
    id="Simple-Snake-48x48-v0",
    entry_point="snake_env.envs.factory:BasicEnv48x48",
)

register(
    id="Simple-Snake-64x64-v0",
    entry_point="snake_env.envs.factory:BasicEnv64x64",
)

# Near Envs
register(
    id="Near-Snake-36x36-v0",
    entry_point="snake_env.envs.factory:NearEnv36x36",
)

register(
    id="Near-Snake-48x48-v0",
    entry_point="snake_env.envs.factory:NearEnv48x48",
)

register(
    id="Near-Snake-64x64-v0",
    entry_point="snake_env.envs.factory:NearEnv64x64",
)
