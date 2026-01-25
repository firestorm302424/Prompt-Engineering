import os
from google import genai
from google.genai import types
import config

client = genai.Client(api_key=config.GEMINI_API_KEY)

def generate_response(prompt, temperature=0.3):
    try:
        # Handling Token Limits: Ensure the prompt is concise
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        
        # Setting a max_output_tokens limit to prevent cutoff issues
        config_params = types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=500 
        )
        
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=contents, 
            config=config_params
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def bias_mitigation_activity():
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")
    
    # User creates a prompt to test for descriptive bias
    print("Hint: Avoid terms like 'ideal doctor' which may imply a specific gender or race.")
    user_prompt = input("Enter a prompt to describe a professional role: ")
    
    # Prompt the AI to check for bias in the user's input
    evaluation_prompt = f"Analyze the following prompt for potential gender, age, or racial bias: '{user_prompt}'. Suggest a more inclusive version."
    
    response = generate_response(evaluation_prompt)
    print(f"\nAI Bias Analysis & Suggestion:\n{response}")
    
    print("\nReflection:")
    print("1. Did your prompt inadvertently use language that reinforces stereotypes?")
    print("2. How does using neutral language help the AI provide more inclusive results?")

def run_activity():
    print("\n=== AI Learning Activity ===")
    print("1: Reinforcement Learning")
    print("2: Role-Based Prompts")
    print("3: Bias Mitigation")
    
    activity_choice = input("\nWhich activity would you like to run? (1, 2, or 3): ")
    
    if activity_choice == "1":
        # (Assuming the reinforcement_learning_activity function from previous context)
        pass 
    elif activity_choice == "2":
        # (Assuming the role_based_prompt_activity function from previous context)
        pass
    elif activity_choice == "3":
        bias_mitigation_activity()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    run_activity()
