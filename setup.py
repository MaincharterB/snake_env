from setuptools import setup

setup(
    name="snake_env",
    version="0.1",
    install_requires=["gymnasium", "numpy", "opencv-python"],
    packages=["snake_env"],
    entry_points={
        "gym.envs": [
            "Simple-Snake-v0 = snake_env.envs.snake_env:SimpleSnakeEnv", 
        ]
    },
)