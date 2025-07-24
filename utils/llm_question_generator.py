import os
import re
import json
import google.generativeai as genai
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_json_array(text: str) -> List[Dict]:
    """
    Extract JSON array from the Gemini response text using regex.
    """
    try:
        match = re.search(r"\[\s*{.*}\s*]", text, re.DOTALL)
        if not match:
            print("❌ No JSON array found in Gemini response.")
            return []
        json_str = match.group(0)
        return json.loads(json_str)
    except Exception as e:
        print(f"❌ Failed to parse JSON array: {e}")
        return []

def generate_llm_questions(topic: str) -> List[Dict]:
    prompt = f"""
You are an expert tutor creating multiple-choice questions for students.

Generate 9 questions for the topic: "{topic}", divided by levels:
- 3 Easy
- 3 Medium
- 3 Hard

Each question must be a JSON object:
- "question": string
- "options": list of 4 strings
- "answer": correct option from the list
- "level": one of "easy", "medium", or "hard"

Return only a JSON array of 9 such question objects.
"""

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    text = response.text.strip()
    print("🔹 Raw Gemini Response Start:\n", text[:300])  # Debug first few lines

    questions = extract_json_array(text)

    if not questions:
        print("⚠️ No valid questions extracted.")
    return questions
