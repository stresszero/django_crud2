from django.urls import path

from movies.models import ActorMovie
from .views import ActorView, MovieView, ActorMovie

urlpatterns = [
    path('view-actor/', ActorView.as_view()),
    path('view-movie/', MovieView.as_view()),
    path('view-actor-movie/', ActorMovie.as_view()),
]
