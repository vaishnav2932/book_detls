from django.db import models

# Create your models here.

class Employee(models.Model):
    email=models.EmailField(null=True)
    uname=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)

class student(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)

class Book(models.Model):
    title=models.CharField(max_length=50)
    genre=models.CharField(max_length=30)
    author=models.CharField(max_length=30)  

    def __str__(self):
        return self.title
    
    def __str__(self) :
        return self.author
    
    def __str__(self) :
        return self.genre
    
 
    