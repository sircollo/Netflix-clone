from django.shortcuts import render
from .requests import *
from tmdb import TMDB
# Create your views here.
# tmdb = TMDB()
def home(request):
  popular_movies = get_movies('popular')[:6]
  upcoming_movies = get_movies('upcoming')[:6]
  # trending_movies = get_movies('trending')
  tv_shows = get_tv_show('popular')[:12]
  title = 'Home of Movies'
  context = {'popular':popular_movies,'upcoming':upcoming_movies,'title':title,'shows':tv_shows}
  
  return render(request, 'index.html', context)

