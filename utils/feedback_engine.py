from utils.gemini_api import call_gemini


def get_feedback_score(user_answer: str, correct_answer: str) -> dict:
    prompt = f"""
You are an educational evaluator.
Evaluate the following student's answer compared to the correct one.

Student's answer:
\"\"\"{user_answer}\"\"\"

Correct answer:
\"\"\"{correct_answer}\"\"\"

Respond with:
1. A score out of 10.
2. A short and helpful feedback message.

Use this format:
Score: <score>
Feedback: <message>
"""

    response = call_gemini(prompt)
    
    # Example response: "Score: 7\nFeedback: You covered the main idea but missed Newton's third law."
    try:
        lines = response.strip().splitlines()
        score = float(lines[0].split(":")[1].strip())
        feedback = lines[1].split(":", 1)[1].strip()
    except Exception:
        score = 0.0
        feedback = "⚠️ Could not extract score/feedback from Gemini."

    return {
        "score": score,
        "feedback": feedback
    }
