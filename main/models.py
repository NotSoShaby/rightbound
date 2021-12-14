from django.db import models
from django.contrib.auth.models import User


class Campaign(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    prospects = models.ManyToManyField('main.Prospect', related_name='campaigns')
    config = models.JSONField(default=dict)


class Prospect(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    linkedin_link = models.URLField()


