from django.db import models
#from django.contrib.auth.models import User

class Author(models.Model):
    AuthorID = models.CharField(max_length = 30)
    Name = models.CharField(max_length = 30)
    Age = models.IntegerField()
    Country = models.CharField(max_length = 30)
    
class Book(models.Model):
    ISBN = models.CharField(max_length = 13)
    Title = models.CharField(max_length = 30)
    Author = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 30)
    PublishDate = models.CharField(max_length = 50)
    Price = models.FloatField()

