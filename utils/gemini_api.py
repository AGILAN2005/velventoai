import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
except KeyError:
    print("❌ Error: GEMINI_API_KEY not found in environment variables.")
    exit()

def call_gemini(prompt: str, model_name="gemini-1.5-flash") -> str:
    print("📤 Sending prompt:", prompt)

    try:
        model = genai.GenerativeModel(model_name=model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ An error occurred: {e}"
