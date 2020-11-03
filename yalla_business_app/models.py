from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings

from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    profile_pic = models.TextField()
    location = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    
    def __str__(self):
        return self.username

class Store(models.Model):
    store_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pro_pic = models.TextField()
    store_name = models.CharField(max_length=64)
    review_rank = models.IntegerField() # Number of stars
    opening_times = models.CharField(max_length=64)
    price_range = models.CharField(max_length=64)
    images=models.TextField()
    store_location=models.CharField(max_length=64)
    pro_pic = models.TextField()
    store_description = models.TextField()
    price = models.IntegerField()
    phone_number = models.IntegerField()
    RESTURANT = 'Resturant'
    CLOTHES = 'Clothes'
    SERVICES = 'Services'
    FASHION = 'Fashion'
    BEAUTY = 'Beauty'
    ENTERTAINMENT = 'Entertainment'
    EDUCATION = 'Education'
    ELECTRICAL = 'Electrical'

    YALLA_CHOICES = [
        (RESTURANT, 'Resturant'),
        (CLOTHES, 'Clothes'),
        (SERVICES, 'Services'),
        (FASHION, 'Fashion'),
        (BEAUTY, 'Beauty'),
        (ENTERTAINMENT, 'Entertainment'),
        (EDUCATION, 'Education'),
        (ELECTRICAL, 'Electrical'),

    ]
    catagories = models.CharField(
        max_length=20,
        choices=YALLA_CHOICES,
        default=EDUCATION,
    )



    
    def __str__(self):
        return self.store_name

class Review(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    store_location = models.TextField()
    store_pic = models.CharField(max_length=64)
    comment = models.TextField()
    review_rate = models.IntegerField()

    
    def __str__(self):
        return self.comment