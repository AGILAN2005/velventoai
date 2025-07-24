

def generate_prompt(user_data):
    topic = user_data["topic"]
    theta = user_data["irt_score"]
    wrong_qs = [x["question"] for x in user_data["history"] if not x["correct"]][-3:]
    wrong_str = "; ".join(wrong_qs) if wrong_qs else "none"
    
    return (
        f"You are a tutor helping a student learn '{topic}'. "
        f"The student has a current ability score of {theta}. "
        f"They previously struggled with: {wrong_str}. "
        f"Generate a single, clear, new conceptual question to help them improve."
    )
