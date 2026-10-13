from django.db import models

# Create your models here.
class Field(models.Model):
    customer_name = models.CharField(max_length=100)
    food_item = models.CharField()
    quantity = models.IntegerField(max_length=100)
    price = models.IntegerField()
    is_delivered = models.BooleanField()