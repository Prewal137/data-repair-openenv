import os
from dotenv import load_dotenv
from openai import OpenAI

from my_env.env import DataRepairEnv
from my_env.models import Action

# -------------------------
# LOAD ENV VARIABLES
# -------------------------
load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

# -------------------------
# OPENAI CLIENT (MANDATORY)
# -------------------------
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

# -------------------------
# CONFIG
# -------------------------
TASKS = ["easy", "medium", "hard"]
MAX_STEPS = 5


# -------------------------
# RUN TASKS
# -------------------------
for task in TASKS:

    env = DataRepairEnv(task)
    obs = env.reset()

    print(f"[START] task={task} env=data_repair_env model={MODEL_NAME}")

    rewards = []
    done = False
    step = 0

    while not done and step < MAX_STEPS:
        step += 1

        try:
            # -------------------------
            # PROMPT
            # -------------------------
            prompt = f"""
You are a data cleaning agent.

Task: {obs.task_type}
Data: {obs.table}

Give the best action to improve dataset.
"""

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}]
            )

            action_text = response.choices[0].message.content.strip()

            action = Action(
                action_type="auto",
                content=action_text
            )

            obs, reward, done, info = env.step(action)

            rewards.append(reward)

            print(f"[STEP] step={step} action={action_text} reward={reward:.2f} done={str(done).lower()} error=null")

        except Exception as e:
            print(f"[STEP] step={step} action=error reward=0.00 done=true error={str(e)}")
            done = True

    score = sum(rewards) / len(rewards) if rewards else 0.0

    print(f"[END] success={str(score>0.5).lower()} steps={step} score={score:.2f} rewards={','.join([f'{r:.2f}' for r in rewards])}")