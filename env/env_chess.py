from typing import Optional, Tuple
import gym
import numpy as np
from gym import spaces, core
from gym.core import ObsType


class env_chess(gym.Env):
    def __init__(self):
        self.action_space = spaces.Discrete(8 * 8)
        # 观测空间
        self.observation_space = spaces.Box(low=-6, high=6, shape=(64,), dtype=np.float32)


    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[dict] = None,
    ) -> Tuple[ObsType, dict]:

        return []

    def step(
            self,
            action: int,
    ):
        start_sq = action // 2
        

        return [], [], True, {}

