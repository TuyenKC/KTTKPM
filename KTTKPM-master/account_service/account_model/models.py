from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.TextField(null=False, blank='')
    password = models.TextField(null=False, blank='')
    email = models.EmailField(null=False, blank='', default="")
    sdt = models.TextField(null=True, blank='')
    location = models.TextField(null=True, blank='')
    fullname = models.TextField(null=True, blank='')

    def __str__(self):
        return self.username