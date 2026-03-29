import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

# Load root .env file specifically
load_dotenv(find_dotenv())

def get_text(genre):
    # Retrieve the consolidated API key from the environment
    api_key = os.getenv("GOOGLE_API_KEY") 
    
    if not api_key:
        print("ERROR: GOOGLE_API_KEY not found in environment!")
        return "I'm sorry, I'm having a little trouble finding my magic storybook! 🌈"
    
    # Configure Google Generative AI
    genai.configure(api_key=api_key)

    # Set up generation configuration
    generation_config = {
        "temperature": 0.8, # Slightly higher for more creative story-telling
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 2048,
        "response_mime_type": "text/plain",
    }

    # Initialize model
    model = genai.GenerativeModel(
        model_name="models/gemini-3-flash-preview", 
        generation_config=generation_config,
        system_instruction="You are a warm, imaginative children's storyteller. You write engaging stories with a moral at the end.",
    )

    # Improved prompt to ensure length and moral in ONE go
    prompt = (
        f"Please write a {genre} story for children. "
        "The story should be at least 250 words long, structured with clear paragraphs, and conclude with a distinct 'Moral of the Story' section. "
        "Ensure the language is simple yet descriptive."
    )

    try:
        response = model.generate_content(prompt)
        model_response = response.text.strip()
        
        # Professional line break handling (if needed)
        # Instead of crude .replace(". ", ".\n"), we rely on the model for paragraphing
        return model_response
    except Exception as e:
        print(f"Story Generation Error: {e}")
        return "I'm sorry, I couldn't come up with a story right now. Let's try again in a moment!"

