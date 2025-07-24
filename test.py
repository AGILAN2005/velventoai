import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

try:
    # Configure the API key.
    # The SDK will automatically pick up the GEMINI_API_KEY from environment variables.
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
except KeyError:
    print("Error: GEMINI_API_KEY environment variable not set.")
    print("Please set your API key as an environment variable or create a .env file.")
    exit()

def generate_gemini_response(prompt_text, model_name="gemini-1.5-flash"):
    """
    Generates a response from the Gemini API for a given prompt.

    Args:
        prompt_text (str): The text prompt for the Gemini model.
        model_name (str): The name of the Gemini model to use.
                          (e.g., "gemini-1.5-flash").
                          'gemini-1.5-pro' is more capable but has stricter
                          free-tier quotas and might lead to rate limit errors.

    Returns:
        str: The generated text response, or an error message.
    """
    try:
        # Initialize the GenerativeModel
        model = genai.GenerativeModel(model_name=model_name)

        # Generate content
        response = model.generate_content(prompt_text)

        # Return the generated text
        return response.text

    except Exception as e:
        # This will catch specific API errors like quota issues.
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Example Usage:

    # --- Using the most reliable free-tier model: gemini-1.5-flash ---
    # This model is generally good for most tasks and has more generous
    # free-tier quotas, making it less likely to hit rate limits quickly.
    user_prompt_1 = "What are the key differences between a black hole and a wormhole?"
    print(f"User Prompt: {user_prompt_1}\n")
    response_text_1 = generate_gemini_response(user_prompt_1, model_name="gemini-1.5-flash")
    print("Generated Response (gemini-1.5-flash):")
    print(response_text_1)
    print("-" * 30)

    user_prompt_2 = "Write a short, uplifting haiku about new beginnings."
    print(f"User Prompt: {user_prompt_2}\n")
    response_text_2 = generate_gemini_response(user_prompt_2, model_name="gemini-1.5-flash")
    print("Generated Response (gemini-1.5-flash):")
    print(response_text_2)
    print("-" * 30)

    user_prompt_3 = "Tell me an interesting fact about the ocean."
    print(f"User Prompt: {user_prompt_3}\n")
    response_text_3 = generate_gemini_response(user_prompt_3, model_name="gemini-1.5-flash")
    print("Generated Response (gemini-1.5-flash):")
    print(response_text_3)
    print("-" * 30)

    # --- Example of trying gemini-1.5-pro (use with caution for free tier) ---
    # This is commented out to prevent immediate quota issues, but you can uncomment
    # if you want to test and are aware of potential rate limits.
    # user_prompt_4 = "Explain quantum entanglement in simple terms."
    # print(f"User Prompt: {user_prompt_4}\n")
    # response_text_4 = generate_gemini_response(user_prompt_4, model_name="gemini-1.5-pro")
    # print("Generated Response (gemini-1.5-pro):")
    # print(response_text_4)
    # print("-" * 30)

    print("\nScript execution complete. If you encountered errors, check your API key and quotas.")