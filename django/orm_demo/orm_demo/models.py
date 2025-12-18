from django.db import models

class Dish(models.Model):
    id = models.AutoField
    name = models.TextField
    price = models.DecimalField
    