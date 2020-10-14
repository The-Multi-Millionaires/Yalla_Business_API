from rest_framework import serializers

from .models import StoreProfile

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'pro_pic', 'store_name', 'review_rank', 'openning_time','price_range','images','store_location')
        model = StoreProfile


    #         store_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # pro_pic = models.TextField()

    # store_name = models.CharField(max_length=64)
    # review_rank = models.IntegerField() # Number of stars
    # openning_time = models.CharField(max_length=64)
    # # close_time = models.TimeField(auto_now_add=True)
    # price_range = models.CharField(max_length=64)
    # images=models.TextField()
    # store_location=models.CharField(max_length=64)