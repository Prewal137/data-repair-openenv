from .models import Observation, Action
from .tasks import get_task
from .graders import grade, compute_quality


class DataRepairEnv:

    def __init__(self, task_name="easy"):
        self.task_name = task_name
        self.task = get_task(task_name)
        self.steps = 0
        self.done = False
        self.quality = compute_quality(self.task["table"])

    # -------------------------
    # RESET → start new episode
    # -------------------------
    def reset(self):
        self.steps = 0
        self.done = False
        self.task = get_task(self.task_name)
        self.quality = compute_quality(self.task["table"])

        return Observation(
            table=self.task["table"],
            quality_score=self.quality,
            task_type=self.task_name
        )

    # -------------------------
    # STEP → take action
    # -------------------------
    def step(self, action: Action):
        self.steps += 1

        prev_quality = self.quality

        # get reward
        reward = grade(self.task, action, prev_quality)

        # update quality (simulate improvement)
        self.quality = min(prev_quality + reward * 0.2, 1.0)

        # done conditions
        if self.steps >= 5 or reward > 0.9:
            self.done = True

        return (
            Observation(
                table=self.task["table"],
                quality_score=self.quality,
                task_type=self.task_name
            ),
            float(reward),
            self.done,
            {"quality": self.quality}
        )

    # -------------------------
    # STATE → current state
    # -------------------------
    def state(self):
        return {
            "task": self.task,
            "quality": self.quality,
            "steps": self.steps
        }