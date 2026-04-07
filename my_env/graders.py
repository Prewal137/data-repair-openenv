def compute_quality(table):
    total = len(table) * len(table[0])
    correct = 0

    for row in table:
        for v in row.values():
            if v not in [None, "", "invalid"] and not (isinstance(v, int) and v < 0):
                correct += 1

    return correct / total


def grade(task, action, prev_score):

    score = 0.0

    content = action.content.lower()

    # -------------------------
    # EASY → Detect issues
    # -------------------------
    if task["type"] == "detect":
        for issue in task["issues"]:
            if issue in content:
                score += 0.5
        return min(score, 1.0)

    # -------------------------
    # MEDIUM → Fix dataset
    # -------------------------
    elif task["type"] == "fix":
        if "fix" in content:
            score += 0.5
        if "correct" in content or "updated" in content:
            score += 0.5
        return min(score, 1.0)

    # -------------------------
    # HARD → Strategy decision
    # -------------------------
    elif task["type"] == "decide":
        if task["strategy"] in content:
            return 1.0
        elif "remove" in content or "fill" in content:
            return 0.5
        else:
            return 0.0

    return 0.0