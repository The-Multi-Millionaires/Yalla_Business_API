from rest_framework import serializers

from .models import Store, UserProfile, Review

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('store_id', 'pro_pic','store_name','review_rank','opening_times','price_range','images','store_location')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user_id', 'username','profile_pic','location','description')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('user_id', 'store_name','store_location','store_pic','comment', 'review_rate')

    