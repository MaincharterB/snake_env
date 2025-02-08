from snake_env.renderers.renderers import HumanRenderer, RGBArrayRenderer, Renderer


def get_renderer(render_mode: str, **kwargs) -> Renderer:
    if render_mode == "human":
        return HumanRenderer(kwargs['observator'])
    elif render_mode == "rgb_array":
        return RGBArrayRenderer(kwargs['observator'])
    else:
        raise ValueError(f"Unknown render mode: {render_mode}")