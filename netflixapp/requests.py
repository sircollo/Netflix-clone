import urllib,json
from .models import *
from django.db import models
import requests



base_url = "https://api.themoviedb.org/3/movie/{}?api_key={}"


def get_movies(category):

    get_movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)
        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

        print(movie_results)
    return movie_results
  
def process_results(movie_list):
    movie_results = []
    for movie_item in movie_list:
        num = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(num,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)
            # print(poster)
    return movie_results
  
tv_base_url = "https://api.themoviedb.org/3/tv/{}?api_key={}"

def get_tv_show(category):

    get_movies_url = tv_base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)
        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)


    return movie_results
  
def process_results(movie_list):
    movie_results = []
    for movie_item in movie_list:
        num = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(num,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)
            # print(poster)
    return movie_results