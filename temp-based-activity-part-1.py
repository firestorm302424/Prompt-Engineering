import os
import time
from google import generativeai as genai
from google.generativeai import types
import config

def generate_response(prompt, temperature=0.5):
    """Generate a response from Gemini API with a specified temperature."""
    try:
        client = genai.Client(api_key=config.GEMINI_API_KEY)
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=prompt)
                ],
            ),
        ]

        generate_content_config = types.GenerateContentConfig(
            temperature=temperature,
            reponse_mime_type="text/plain",
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config=generate_content_config,
        )

        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"
    
def temperature_prompt_activity():
    """Interactive activity to explor temperature settings and instruction-based prompts."""
    print("="*80)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE & INSTRUCTION-BASED PROMPTS")
    print("="*80)
    print("\nIn this activity, we'll explore:")
    print("1. How temperature affects AI creativity and randomness.")
    print("2. How instruction-based prompts can control AI outputs.")

    print("\n" + "-" * 40)
    print("PART 1: TEMPERATURE EXPLORATION")
    print("-" * 40)

    base_prompt = input("\nEnter a creative prompt (e.g., 'Write a short story about a robot learning to paint'): ")

    print("\nGenerating responses with different temperature settings...")
    print("\n--- LOW TEMPERATURE (0.1) - MORE DETERMINISTIC ---")
    low_temp_response = generate_response(base_prompt, temperature=0.1)
    print(low_temp_response)

    time.sleep (1)

    print("\n--- MEDIUM TEMPERATURE (0.5) - BALANCED ---")
    medium_temp_response = generate_response(base_prompt, temperature=0.5)
    print(medium_temp_response)

    time.sleep (1)

    print("\n--- HIGH TEMPERATURE (0.9) - MORE RANDOM/CREATIVE ---")
    high_temp_response = generate_response(base_prompt, temperature=0.9)
    print(high_temp_response)
