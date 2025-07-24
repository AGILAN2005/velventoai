def update_irt_score(current_theta, correct):
    learning_rate = 0.1
    return current_theta + learning_rate if correct else current_theta - learning_rate
