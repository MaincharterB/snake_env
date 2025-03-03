import gymnasium as gym
import numpy as np
import cv2

from snake_env.enums.actions import Direction, Status
from snake_env.food_placers.food_placers import FoodPlacer
from snake_env.memory_managers.memory_managers import BasicMemoryManager
from snake_env.observators.observators import BasicObservator
from snake_env.renderers.factory import get_renderer
from snake_env.steppers.steppers import BasicStepper
from snake_env.utils.configs import BaseConfig


class SimpleSnakeEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 60}

    def __init__(self, **args: BaseConfig):
        super(SimpleSnakeEnv, self).__init__()
        self.args = args
        self.render_mode = args.get("render_mode", "rgb_array")
        
        # Action and observation spaces
        self.action_space = gym.spaces.Discrete(len(Direction))
        self.observation_space = gym.spaces.Box(
            low=0, high=255, shape=(args["height"], args["width"], 3), dtype=np.uint8
        )

        # Core game components
        self.memory_manager = BasicMemoryManager(**args)
        self.placer = FoodPlacer(self.memory_manager, **vars(args["food_config"]))
        self.stepper = BasicStepper(self.placer, self.memory_manager)
        self.observator = BasicObservator(self.memory_manager)
        self.renderer = get_renderer(render_mode=self.render_mode, observator=self.observator)

        self.init_snake()

    def init_snake(self):
        req_snake_length = self.args["init_snake_size"]
        snake_pos = []
        snake_head = (self.args["height"] // 2, self.args["width"] // 2)
        snake_pos.insert(0, snake_head)

        direction = Direction.RIGHT if self.args["width"] >= self.args["height"] else Direction.UP
        body_direction = Direction.LEFT if direction == Direction.RIGHT else Direction.DOWN

        for _ in range(req_snake_length):
            new_pos = (snake_pos[-1][0] + body_direction.value[0], snake_pos[-1][1] + body_direction.value[1])
            snake_pos.append(new_pos)

        self.memory_manager["direction"] = direction
        self.memory_manager["snake_positions"] = snake_pos

    def step(self, action):
        if not self.memory_manager["snake_positions"]:
            self.init_snake()

        self.stepper.step(action)

        obs = self.observator.get_observation()
        reward = 1 if self.memory_manager["status"] == Status.EAT_FOOD else 0
        done = self.memory_manager["status"] == Status.DEAD
        truncated = False 
        info = {}

        return obs, reward, done, truncated, info

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.memory_manager.clear()
        self.init_snake()
        self.placer.place_food()
        obs = self.observator.get_observation()
        info = {}

        return obs, info

    def render(self):
        return self.renderer.render()

    def close(self):
        cv2.destroyAllWindows()
