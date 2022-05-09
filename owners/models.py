from django.db import models
from django.core.validators import MinValueValidator


class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=300)
    age = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        db_table = 'owners'


class Dog(models.Model):

    name = models.CharField(max_length=45)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    age = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        db_table = 'dogs'
