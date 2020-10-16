from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



from .forms import CustomUserCreationForm

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework import filters


from .models import Store, UserProfile, Review

from .serializers import StoreSerializer, UserSerializer, ReviewSerializer

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class StoreList(ListCreateAPIView):
    search_fields = ['store_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreDetails(RetrieveUpdateDestroyAPIView):
    # template_name = 'details.html'
    queryset = Store.objects.all()
    serializer_class = StoreSerializer




class UserList(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

class ProfileDetails(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer




class ReviewList(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer