from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.


# # Store profile 
# progile pic/store name/ review / openning time / price range / images / location user reviews

class StoreProfile(models.Model):
    # pro_pic = models.ImageField()

    store_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pro_pic = models.TextField()

    store_name = models.CharField(max_length=64)
    review_rank = models.IntegerField() # Number of stars
    openning_time = models.CharField(max_length=64)
    # close_time = models.TimeField(auto_now_add=True)
    price_range = models.CharField(max_length=64)
    images=models.TextField()
    store_location=models.CharField(max_length=64)
    


    # author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # title = models.CharField(max_length=64)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title

# class store_reviews(models.Model):
#     store_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     user_rate = models.IntegerField()
#     users_reviews = models.TextField()


# user profile
# profile pic / user name / location / bookmarks / bio / reviews



class CustomUser(AbstractUser):

    # user_pro_pic = models.TextField()
    # user_location=models.CharField(max_length=64)
    # bookmarks= models.TextField()
    




    
    # add additional fields in here

    def __str__(self):
        return self.username