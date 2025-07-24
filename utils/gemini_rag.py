import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_summary(feedback_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Summarize the following feedback for educational analysis:\n\n{feedback_text}"
    response = model.generate_content(prompt)
    return response.text
