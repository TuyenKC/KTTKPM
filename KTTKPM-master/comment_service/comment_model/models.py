from django.db import models
from rest_framework import serializers
import requests
# Create your models here.

class Comment(models.Model):
    account = models.CharField(max_length=200)
    product_id = models.CharField(max_length=200)
    itemType = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    rate = models.IntegerField(default=0)

    def __str__(self):
        response = requests.get('http://127.0.0.1:8000/accounts/' + self.account)\
        
        if(self.itemType == 'apparel'):
            response2 = requests.get('http://127.0.0.1:8001/apparels/' + self.product_id)
        if(self.itemType == 'book'):
            response2 = requests.get('http://127.0.0.1:8011/books/' + self.product_id)
        if(self.itemType == 'shoe'):
            response2 = requests.get('http://127.0.0.1:8012/shoes/' + self.product_id)
        if(self.itemType == 'clothe'):
            response2 = requests.get('http://127.0.0.1:8013/clothes/' + self.product_id)
        
        response.raise_for_status()
        response2.raise_for_status()
        account_data = response.json()
        product_data = response2.json()
        username = account_data.get('username', 'Unknown')
        product_name = product_data.get('name', 'Unknown')
        return f'{username} - Product: {product_name}'
