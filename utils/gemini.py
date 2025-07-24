import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_roadmap_stages(topic, urls):
    prompt = f"""
I am creating a personalized learning roadmap for a student interested in "{topic}".

Here are some reference links:
{chr(10).join(urls)}

Please analyze them and return:
1. 🔢 A roadmap broken into 4-6 clearly titled learning stages.
2. 📚 1-2 resources (URLs or concepts) per stage.
3. 📝 Stage summary (2 lines) per stage.
Return the result as a Python list of dictionaries with keys: "stage", "summary", "resources".
"""
    response = model.generate_content(prompt)
    return response.text
