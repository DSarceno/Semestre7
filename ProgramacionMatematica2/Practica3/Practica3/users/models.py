from django.db import models

# Create your models here.


class usuarios(models.Model):
    nickname = models.CharField(max_length = 10)
    email = models.EmailField()
    CUI = models.IntegerField()
    carrera = models.CharField(max_length = 30)
    password = models.CharField(max_length = 15)


class files(models.Model):
    nickname = models.CharField(max_length = 10)
    file = models.FileField(upload_to = 'archivos/')
