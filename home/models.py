from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=132)
    phone=models.CharField( max_length=50)
    desc=models.TextField(max_length=300)
    def __str__(self):
        return self.name
