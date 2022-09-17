from django.db import models

# Create your models here.

class book(models.Model):
    bookid=models.IntegerField(primary_key=True)
    booknm=models.CharField(max_length=100)
    bookpublisher=models.CharField(max_length=100)
    bookpr=models.IntegerField()
