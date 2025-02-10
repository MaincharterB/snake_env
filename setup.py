from setuptools import setup

setup(
    name="snake_env",
    version="0.1",
    install_requires=["gymnasium", "numpy", "opencv-python"],
    packages=["snake_env"],
    entry_points={
        "gym.envs": [
            "Simple-Snake-36x36-v0 = snake_env.envs.factory:BasicEnv36x36", 
            "Simple-Snake-48x48-v0 = snake_env.envs.factory:BasicEnv48x48",
            "Simple-Snake-64x64-v0 = snake_env.envs.factory:BasicEnv64x64",
            #Near envs
            "Near-Snake-36x36-v0 = snake_env.envs.factory:NearEnv36x36",
            "Near-Snake-48x48-v0 = snake_env.envs.factory:NearEnv48x48",
            "Near-Snake-64x64-v0 = snake_env.envs.factory:NearEnv64x64",
        ]
    },
)