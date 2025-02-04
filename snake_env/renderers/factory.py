from snake_env.renderers.renderers import HumanRenderer, RGBArrayRenderer, Renderer


def get_renderer(render_mode: str) -> Renderer:
    if render_mode == "human":
        return HumanRenderer()
    elif render_mode == "rgb_array":
        return RGBArrayRenderer()
    else:
        raise ValueError(f"Unknown render mode: {render_mode}")