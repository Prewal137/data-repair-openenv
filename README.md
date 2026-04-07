# 🚀 Data Repair OpenEnv

AI Environment for Dataset Cleaning & Repair

---

## 📌 Overview

**Data Repair OpenEnv** is a custom AI training environment designed to simulate real-world dataset cleaning tasks.
It enables AI agents to **detect errors, fix data issues, and make intelligent decisions** through structured interactions.

This project is built following OpenEnv standards with:

* Typed models (Observation, Action, Reward)
* Multi-level tasks (easy → medium → hard)
* Deterministic reward system
* Docker-based execution

---

## 🎯 Problem Statement

Real-world datasets often contain:

* Missing values
* Invalid entries (e.g., negative values, wrong data types)
* Inconsistent formats

This environment simulates such scenarios and evaluates how well an AI agent can:

1. Detect issues
2. Repair data
3. Decide optimal cleaning strategies

---

## 🧠 Key Features

### ✅ 1. Structured Environment

* Fully compliant OpenEnv setup
* Supports `reset()`, `step()`, and `state()`

---

### ✅ 2. Multi-Level Tasks

| Level     | Objective                |
| --------- | ------------------------ |
| 🟢 Easy   | Detect data issues       |
| 🟡 Medium | Fix dataset              |
| 🔴 Hard   | Decide cleaning strategy |

---

### ✅ 3. Intelligent Grading System

* Deterministic scoring (0.0 → 1.0)
* Partial rewards
* Flexible natural language evaluation

---

### ✅ 4. Realistic AI Interaction

* Uses LLM via OpenAI-compatible API
* Handles natural language responses
* Simulates real-world data cleaning workflows

---

### ✅ 5. Docker Support

* Fully containerized
* Reproducible execution
* Easy deployment

---

## 🏗️ Project Structure

```
data-repair-openenv/
│
├── my_env/
│   ├── env.py          # Core environment (step/reset/state)
│   ├── models.py       # Observation, Action, Reward
│   ├── tasks.py        # Task definitions
│   ├── graders.py      # Reward logic
│
├── inference.py        # Main execution script
├── openenv.yaml        # Environment metadata
├── Dockerfile          # Container setup
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
```

---

## ⚙️ Setup Instructions

### 🔹 1. Clone Repository

```bash
git clone <your-repo-link>
cd data-repair-openenv
```

---

### 🔹 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 3. Create `.env` File

```env
HF_TOKEN=your_token_here
API_BASE_URL=https://router.huggingface.co/v1
MODEL_NAME=Qwen/Qwen2.5-72B-Instruct
```

---

### 🔹 4. Run Locally

```bash
python inference.py
```

---

## 🐳 Docker Setup

### 🔹 Build Image

```bash
docker build -t data-repair-env .
```

---

### 🔹 Run Container

```bash
docker run --env-file .env data-repair-env
```

---

## 📊 Example Output

```
[START] task=easy ...
[STEP] step=1 ...
[END] success=true score=1.00
```

---

## 🧪 How It Works

1. Environment generates a task
2. LLM suggests an action
3. Grader evaluates response
4. Reward is assigned
5. Process repeats until completion

---

## 🧠 Design Philosophy

This project focuses on:

* **Reinforcement-style learning environments**
* **Reward shaping for AI behavior**
* **Deterministic evaluation**
* **Lightweight simulation (fast + reproducible)**

---

## 🚀 Future Improvements

* Larger datasets
* Multi-table cleaning
* Real-time data pipelines
* Visualization dashboard

---

## 🏁 Conclusion

This project demonstrates how AI agents can be trained and evaluated in a controlled environment for **data cleaning and decision-making tasks**.

It is designed to be:

* Scalable
* Modular
* Hackathon-ready

---

## 🙌 Acknowledgment

Built as part of a hackathon project focusing on:

* AI environments
* Data quality improvement
* LLM-driven automation

---

🔥 *Ready for deployment and evaluation*
