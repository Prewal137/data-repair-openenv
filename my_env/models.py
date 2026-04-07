from pydantic import BaseModel
from typing import List, Dict, Any


# -------------------------
# Observation (state seen by agent)
# -------------------------
class Observation(BaseModel):
    table: List[Dict[str, Any]]
    quality_score: float
    task_type: str


# -------------------------
# Action (what agent sends)
# -------------------------
class Action(BaseModel):
    action_type: str   # detect / fix / decide
    content: str


# -------------------------
# Reward (score returned)
# -------------------------
class Reward(BaseModel):
    value: float