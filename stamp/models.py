from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stamp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stamps = models.JSONField(default=list)