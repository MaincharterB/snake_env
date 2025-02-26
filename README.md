# Snake Environment

## Description
Snake Environment is a reinforcement learning (RL) environment for training and testing RL algorithms on the classic Snake game. The environment supports various configurations, allowing users to model different difficulty levels and adapt it to specific learning tasks.

## Features
- 🟢 Flexible grid size configuration.
- 🍎 Various food generation modes.
- 🔗 Integration with OpenAI Gym API.
- 🎥 Real-time game visualization.

## Installation
```bash
pip install -r requirements.txt
```

## Usages
### Simple Usage
```python
import gymnasium as gym

env = gym.make('Simple-Snake-36x36-v0') # For traditional snake game
near_env = gym.make('Near-Snake-36x36-v0') # For near food snake game
# Reset environment before starting an episode
state, info = env.reset()

done = False
while not done:
    action = env.action_space.sample()  # random action
    next_state, reward, done, truncated, info = env.step(action)
    env.render()

env.close()
```

### Custom Usage
```python
from snake_env.envs.env import SimpleSnakeEnv
from snake_env.utils.configs import BaseConfig, FoodConfig

food_confid = FoodConfig(num_placed_foods_per_episode=1, food_place_strategy='near', food_size=1)
snake_config = BaseConfig(64, 64, render_mode='rgb_array', init_snake_size=6, food_config=food_confid)
env = SimpleSnakeEnv(**vars(snake_config))

state, info = env.reset()

done = False
while not done:
    action = env.action_space.sample()  # random action
    next_state, reward, done, truncated, info = env.step(action)
    env.render()

env.close()
```

## Available Configurations
| Parameter                    | Description                                   | Possible Values                         |
|------------------------------|-----------------------------------------------|-----------------------------------------|
| `height`, `width`            | 📏 Size of the game grid                      | Integer values                          |
| `linked_paths`               | 🔗 Predefined linked paths in the grid        | List of `LinkConfig` objects            |
| `init_snake_size`            | 🐍 Initial size of the snake                  | Integer                                 |
| `max_steps`                  | ⏳ Maximum steps per episode                  | Integer                                 |
| `use_time_limit`             | ⏱️ Whether to enforce a time limit            | `True`, `False`                         |
| `render_mode`                | 🖥️ Rendering mode                             | `human`, `rgb_array`                    |
| `num_placed_foods_per_episode` | 🍏 Number of food pieces placed per episode | Integer                                 |
| `food_place_strategy`        | 🍽️ Strategy for food placement               | `random`, `near`                        |
| `food_size`                  | 🍎 Size of the food                           | Integer or list of integers             |
| `food_reward`                | 🏆 Reward for eating food                     | Float                                   |
| `collision_reward`           | ❌ Penalty for collisions                     | Float                                   |
| `time_reward`                | ⏰ Reward per timestep                        | Float                                   |
| `near_food_reward`           | 👀 Reward for being near food                 | Float                                   |
| `link_from`                  | 🔄 Path link start position                   | Integer                                 |
| `link_direction`             | ➡️ Direction of linked path                   | `TOP`, `BOTTOM`, `LEFT`, `RIGHT`        |
## OpenAI Gym Integration
Snake Environment follows the standard OpenAI Gym interface, making it easy to use in RL agent training.

## Visualization
The `render()` method is available for rendering the game. A headless mode is also available for non-graphical operations.

## TODO
- 🏗️ Add support for complex maps with obstacles.
- 🎮 Implement a multiplayer mode.
- 🍽️ Improve food generation logic.

## License
Apache-2.0 license

