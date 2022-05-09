from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from requests import request
from .models import Owner, Dog
import json


class AddOwner(View):
    def post(self, request):
        input_data = json.loads(request.body)

        owner = Owner.objects.create(
            name=input_data["name"], email=input_data["email"], age=input_data["age"])
        return JsonResponse({"message": "Add Owner SUCCESS"}, status=201)


class AddDog(View):
    def post(self, request):
        input_data = json.loads(request.body)
        owner_data = Owner.objects.get(id=input_data["owner"])
        dog = Dog.objects.create(
            name=input_data["name"], owner=owner_data, age=input_data["age"])

        return JsonResponse({"message": "Add Dog SUCCESS"}, status=201)


class OwnerView(View):
    def get(self, request):
        pass


class DogView(View):
    def get(self, request):
        pass
