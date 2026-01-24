from google import genai
from google.genai import types
import config


# Initialize Gemini Client
client = genai.Client(api_key=config.GEMINI_API_KEY)


def generate_response(prompt, temperature=0.3):
    """
    Generates a response from Gemini model
    """
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(prompt)]
                )
            ],
            config=types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=200
            )
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"


def bias_mitigation_activity():
    """
    Activity to demonstrate bias mitigation
    """
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")

    prompt = input("Enter a prompt that may contain bias:\n")
    print("\nInitial AI Response:\n")
    print(generate_response(prompt))

    neutral_prompt = input("\nRewrite the prompt to be more neutral:\n")
    print("\nNeutral AI Response:\n")
    print(generate_response(neutral_prompt))


def token_limit_activity():
    """
    Activity to demonstrate token limits
    """
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")

    long_prompt = input("Enter a long prompt:\n")
    print("\nAI Response (Token Limited):\n")
    print(generate_response(long_prompt, temperature=0.5))


def main():
    print("\n=== AI LEARNING ACTIVITY ===")
    print("1. Bias Mitigation")
    print("2. Token Limits")

    choice = input("\nChoose activity (1 or 2): ")

    if choice == "1":
        bias_mitigation_activity()
    elif choice == "2":
        token_limit_activity()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
