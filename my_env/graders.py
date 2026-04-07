def compute_quality(table):
    total = len(table) * len(table[0])
    correct = 0

    for row in table:
        for v in row.values():
            if v not in [None, "", "invalid"] and not (isinstance(v, int) and v < 0):
                correct += 1

    return correct / total


def grade(task, action, prev_score):
    """
    Grades the agent's action based on the task type.
    Provides deterministic partial rewards and handles natural language responses.
    Returns a score between 0.0 and 1.0.
    """
    score = 0.0
    content = action.content.lower()

    # Helper function for flexible keyword matching
    def matches(keywords):
        return any(k in content for k in keywords)

    # -------------------------
    # EASY → Detect issues
    # -------------------------
    if task["type"] == "detect":
        # Flexibility: User finds invalid age (combines 'age' with indicators like 'invalid' or 'string')
        age_indicators = ["invalid", "string", "not numeric", "twenty", "type", "non-numeric"]
        has_age_issue = "age" in content and any(k in content for k in age_indicators)
        
        # Flexibility: User finds missing name (combines 'name' with indicators like 'missing' or 'empty')
        name_indicators = ["missing", "empty", "blank", "unspecified", "none", "not provided"]
        has_name_issue = "name" in content and any(k in content for k in name_indicators)

        if has_age_issue and has_name_issue:
            return 1.0
        elif has_age_issue or has_name_issue:
            return 0.5
        else:
            return 0.0


    # -------------------------
    # MEDIUM → Fix dataset
    # -------------------------
    elif task["type"] == "fix":
        # Mentions handling missing values
        missing_val_keywords = ["missing value", "missing data", "null", "nan", "none", "empty"]
        # Mentions fixing negative values
        negative_val_keywords = ["negative", "below zero", "less than zero", "invalid negative"]
        # Proposes fixing strategy (replace/impute/fix)
        strategy_keywords = ["replace", "impute", "fix", "correct", "update", "clean", "fill"]

        if matches(missing_val_keywords):
            score += 0.35
        if matches(negative_val_keywords):
            score += 0.35
        if matches(strategy_keywords):
            score += 0.30
            
        return min(score, 1.0)

    # -------------------------
    # HARD → Strategy decision
    # -------------------------
    elif task["type"] == "decide":
        # Identifies negative values issue
        neg_issue_keywords = ["negative", "below zero", "less than zero", "sign error", "salary < 0"]
        # Identifies missing values issue
        missing_issue_keywords = ["missing", "empty", "null", "nan", "none", "not provided"]
        # Proposes correct strategy (remove/impute/replace)
        strategy_keywords = ["remove", "impute", "replace", "drop", "fill", "strategy"]

        if matches(neg_issue_keywords):
            score += 0.35
        if matches(missing_issue_keywords):
            score += 0.35
        if matches(strategy_keywords):
            score += 0.30
            
        return min(score, 1.0)

    return 0.0