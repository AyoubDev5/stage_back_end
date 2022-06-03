from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role =models.CharField(max_length=255,default='user')
    username = None    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Department(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)

class Project(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)
    description = models.TextField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default = True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    department =  models.ForeignKey(Department, on_delete=models.CASCADE)

class Employee(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    specialite = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Tache(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default = True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.CharField(max_length=255)
    employee =  models.ForeignKey(Employee, on_delete=models.CASCADE)
    project =  models.ForeignKey(Project, on_delete=models.CASCADE)

class Material(models.Model):
    name = models.CharField(max_length=255)
    prix = models.FloatField ()
    quantity = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)