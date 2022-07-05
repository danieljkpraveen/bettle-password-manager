from django.db import models
from manage import base_django
base_django()


class LoginModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    security_question_one = models.TextField()
    security_question_two = models.TextField()
    
class UserCredentialsModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.URLField()
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    
    