from django.urls import path
from .views import AddOwner, AddDog, OwnerView, DogView

urlpatterns = [
    path('add-owner/', AddOwner.as_view()),
    path('add-dog/', AddDog.as_view()),
    path('view-owner/', OwnerView.as_view()),
    path('view-dog/', DogView.as_view())
]
