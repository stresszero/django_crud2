from django.urls import path
from .views import AddOwner, AddDog, OwnerDogView, OwnerView, DogView

urlpatterns = [
    path('add-owner/', AddOwner.as_view()),
    path('add-dog/', AddDog.as_view()),
    path('view-owner/', OwnerView.as_view()),
    path('view-dog/', DogView.as_view()),
    path('view-ownerdog/', OwnerDogView.as_view())
]
