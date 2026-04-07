def get_task(name):

    # -------------------------
    # EASY TASK → Detect Issues
    # -------------------------
    if name == "easy":
        return {
            "type": "detect",
            "table": [
                {"name": "John", "age": "twenty"},
                {"name": "", "age": 25}
            ],
            "issues": ["invalid_age", "missing_name"]
        }

    # -------------------------
    # MEDIUM TASK → Fix Data
    # -------------------------
    elif name == "medium":
        return {
            "type": "fix",
            "table": [
                {"name": "Alice", "age": None},
                {"name": "Bob", "age": -5}
            ],
            "clean_table": [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25}
            ]
        }

    # -------------------------
    # HARD TASK → Decision Making
    # -------------------------
    elif name == "hard":
        return {
            "type": "decide",
            "table": [
                {"name": "X", "salary": -1000},
                {"name": "Y", "salary": None}
            ],
            "strategy": "remove_negative_and_fill_missing"
        }

    else:
        raise ValueError("Invalid task name")