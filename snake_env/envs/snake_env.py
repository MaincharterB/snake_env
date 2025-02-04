import gymnasium as gym
import numpy as np

from snake_env.enums.actions import BaseActions
from snake_env.food_placers.factory import get_placer
from snake_env.observators.observators import BasicObservator
from snake_env.renderers.factory import get_renderer
from snake_env.steppers.steppers import BasicStepper
from snake_env.utils.configs import BaseConfig
class SimpleSnakeEnv(gym.Env):
    metadata = {'render_modes': ['human', 'rgb_array'], 'render_fps': 60}
    
    def __init__(self, **args: BaseConfig):
        super(SimpleSnakeEnv, self).__init__()
        self.action_space = gym.spaces.Discrete(len(BaseActions))
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(args['height'], args['width'], 3), dtype=np.uint8)
        self.args = args
        self.renderer = get_renderer(args['render_mode'])
        self.placer =  get_placer(args['food_config'])
        self.stepper = BasicStepper()
        self.observator = BasicObservator()
        
    def step(self, action):
        return super().step(action)
    
    def reset(self, seed=None, options=None):
        return super().reset(seed=seed, options=options)
    
    def render(self):
        return self.renderer.render(self.observation)    