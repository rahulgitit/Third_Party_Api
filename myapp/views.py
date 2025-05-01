from django.shortcuts import render
import requests
import json
from django.http import JsonResponse

API_KEY='c398bb18fdda4dad9975a457a296b6c2'
# Create your views here.



def home(request):
    country=request.GET.get('country')
    category=request.GET.get('category')


    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    return render(request, 'home.html',{'articles': articles})  # Return JSON response for the API endpoint
    