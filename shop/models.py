from django.db import models

# Create your models here.

class ShopCard(models.Model):
    imageCard = models.ImageField(upload_to='img/') 
    description = models.TextField(blank=True,null=True)
    titleCard = models.CharField(max_length=200)
    priceCard = models.IntegerField()

    def __str__(self):
        return self.titleCard


