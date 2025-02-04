from snake_env.food_placers.food_placers import FoodPlacer, NearFoodPlacer, RandomFoodPlacer
from snake_env.utils.configs import FoodConfig


def get_placer(food_config: FoodConfig) -> FoodPlacer:
    if food_config.food_place_strategy == "random":
        return RandomFoodPlacer(**food_config.__dict__)
    elif food_config.food_place_strategy == "near":
        return NearFoodPlacer(**food_config.__dict__)
    else:
        raise ValueError(f"Unknown food place strategy: {food_config.food_place_strategy}")