from django.shortcuts import render
from django.http import JsonResponse

from .utils import get_text

def index(request):
    genrelist = ["fantasy", "thriller", "fiction", "adventure", "fairytale"]
    return render(request, 'index.html',{'genrelist': genrelist})

def story(request, genre):
    # Call the AI generator instead of using placeholders
    story_text = get_text(genre)
    return render(request, 'story.html', {'genre': genre, 'story': story_text})

def get_story(request, genre):
    # API endpoint using the AI generator
    story_text = get_text(genre)
    return JsonResponse({'story': story_text})
