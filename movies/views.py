from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from requests import request
from .models import Actor, Movie, ActorMovie
import json


class ActorView(View):
    def get(self, request):
        results = []
        actors = Actor.objects.all()
        for actor in actors:
            movie_list = []
            movies = actor.movies.all()  # Movie 모델의 related_name='movies' 사용
            for movie in movies:
                movie_list.append(movie.title)
            results.append(
                {
                    "성": actor.last_name,
                    "이름": actor.first_name,
                    "출연한 영화": movie_list,
                }
            )
        return JsonResponse({'results': results}, status=200)


class MovieView(View):
    def get(self, request):
        results = []
        movies = Movie.objects.all()
        for movie in movies:
            actor_list = []
            actors = movie.actors.all()
            for actor in actors:
                actor_list.append(actor.last_name + actor.first_name)
            results.append({
                "제목": movie.title,
                "상영시간": movie.running_time,
                "출연한 배우": actor_list,
            })

        return JsonResponse({'results': results}, status=200)


class ActorMovie(View):
    pass


class AddActor(View):
    pass


class AddMovie(View):
    pass
