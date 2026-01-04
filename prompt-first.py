from google import genai
from config import GEMINI_API_KEY

client=genai.Client(api_key=GEMINI_API_KEY)

def generate_response(prompt):
    response=client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

def silly_prompt():
    print("Welcome to the Ai prompt engineering tutorial")
    print("In this activity, we will learn about clarity and specificity and contextual information in crafting prompts for ai")

    print("Lets start by crafting a vague prompt, making it more specific, tben addidnt context")

    vague_prompt=input("Please enter a vague prompt: ")
    vague_response=generate_response(vague_prompt)
    print(f"Your prompt is {vague_prompt}")
    print(vague_response)

    specific_prompt=input("Now make the prompt more specific: ")

    print(f"Your specific prompt: {specific_prompt}")
    specific_response=generate_response(specific_prompt)
    print(specific_response)

    contextual_prompt=input("Now add context to your specific prompt: ")
    print(f"Your contextual prompt: {contextual_prompt}")
    contextual_response=generate_response(contextual_prompt)
    print(contextual_prompt)

    print("Reflection")

    print("1. How did the AI's response change when the prompt was made more specific?")
    
    print("2. How did the AI's response improve with the added context?")

    print("3. Which prompt produced the most relevant and tailored response? Wny?")

silly_prompt()