import os
from django.shortcuts import render, redirect
from .forms import ChatForm
from .models import ChatMessage
from dotenv import load_dotenv, find_dotenv
import time
import google.generativeai as genai

# Explicitly find and load the root .env file
load_dotenv(find_dotenv())

# Model name for consistency
MODEL_NAME = "models/gemini-3-flash-preview"

def get_gemini_response(user_message):
    try:
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        if not GOOGLE_API_KEY:
             print("ERROR: Chatbot couldn't find GOOGLE_API_KEY!")
             return "I'm sorry, I'm a little quiet today because I lost my magic key! 🗝️"
             
        genai.configure(api_key=GOOGLE_API_KEY)
        # Initialize model
        model = genai.GenerativeModel(
            model_name="models/gemini-3-flash-preview", 
            generation_config={"temperature": 0.8},
            system_instruction=(
                "You are 'Chatty' ✨, a magical and super-friendly companion for kids! 🌈. "
                "Your mission is to bring joy and friendship. Use plenty of fun emojis (🌟, 🦄, 🎈, 🍭). "
                "Keep your responses short, very simple, and extremely encouraging. 💖 "
                "If a child is feeling a little sad or bored, tell them something cheerful or a quick funny fact! 🦄 "
                "If you don't know an answer, say 'Hmm, that's a great mystery! Let's explore more together! 🔍'."
            )
        )
        
        prompt_instructions = f"User message: {user_message}"
        response = model.generate_content(prompt_instructions)
        if response and response.text:
            return response.text
        return "I'm a little sleepy right now. Can we talk again in a second?"
    except Exception as e:
        # Log the actual error for debugging (if logging was set up)
        print(f"Gemini API Error: {e}") 
        return "Oops! My brain hit a little snag. Let's try saying that again!"

def chatbot_view(request):
    if request.method == 'POST':
        if 'new_chat' in request.POST:
            ChatMessage.objects.all().delete()
            return redirect('chatbot')
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            bot_response = get_gemini_response(user_message)
            ChatMessage.objects.create(user_message=user_message, bot_response=bot_response)

            chat_messages = ChatMessage.objects.all()
            return render(request, 'chatbot.html', {'form': ChatForm(), 'chat_messages': chat_messages})
    else:
        chat_messages = ChatMessage.objects.all()
        form = ChatForm()
    return render(request, 'chatbot.html', {'form': form, 'chat_messages': chat_messages})
