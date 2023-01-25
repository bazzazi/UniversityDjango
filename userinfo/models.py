from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    age=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name