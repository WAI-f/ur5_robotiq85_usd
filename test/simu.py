import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Open grasp_scene.usd in Isaac Sim and simulation."
    )

    parser.add_argument("--usd", 
                        type=str,
                        help="usd file full path"
    )

    parser.add_argument("--headless",
                        action="store_true",
                        help="run without isaac sim GUI"
    )
    
    parser.add_argument(
        "--steps",
        type=int,
        default=0,
        help="number of simulation step, 0 means run until simulation close."
    )

    return parser.parse_args()

args = parse_args()

from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless":args.headless})

import carb
import omni.usd
from isaacsim.core.api import World
from isaacsim.core.utils.stage import is_stage_loading, open_stage
import os

def wait_for_stage():
    while is_stage_loading():
        simulation_app.update()


if __name__ == "__main__":
    usd_path = args.usd

    try:
        if not os.path.isfile(usd_path):
            raise FileNotFoundError(f"USD scene does not exist: {usd_path}")
        carb.log_info(f"Opening USD scene: {usd_path}")

        open_stage(usd_path)
        wait_for_stage()

        stage = omni.usd.get_context().get_stage()
        if stage is None:
            raise RuntimeError(f"Failed to open USD scene: {usd_path}")
        carb.log_info(f"Opened USD scene: {usd_path}")

        world = World(stage_units_in_meters=1.0)
        world.reset()

        step_count = 0
        run_forever = args.steps <= 0
        while simulation_app.is_running() and (run_forever or step_count < args.steps):
            world.step(render=True)
            step_count += 1
    finally:
        simulation_app.close()