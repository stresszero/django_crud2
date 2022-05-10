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
        # owner input을 name으로 받으려면 .get(name=input_date["owner"])
        dog = Dog.objects.create(
            name=input_data["name"], owner=owner_data, age=input_data["age"])

        return JsonResponse({"message": "Add Dog SUCCESS"}, status=201)


class OwnerView(View):
    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            results.append(
                {
                    "이름": owner.name,
                    "이메일": owner.email,
                    "나이": owner.age,
                }
            )
        return JsonResponse({'results': results}, status=200)


class DogView(View):
    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        for dog in dogs:
            results.append(
                {
                    "이름": dog.name,
                    "나이": dog.age,
                    "주인이름": dog.owner.name,
                }
            )
        return JsonResponse({'results': results}, status=200)


class OwnerDogView(View):
    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            dogs = Dog.objects.filter(owner_id=owner.id)
            dog_list = []
            for dog in dogs:
                dog_data = {"이름": dog.name, "나이": dog.age}
                dog_list.append(dog_data)
            results.append(
                {
                    "이름": owner.name,
                    "이메일": owner.email,
                    "나이": owner.age,
                    "키우는 강아지": dog_list,
                }
            )
        return JsonResponse({'results': results}, status=200)
