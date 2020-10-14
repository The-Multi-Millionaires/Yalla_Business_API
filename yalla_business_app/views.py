from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

from rest_framework.generics import ListCreateAPIView
from .models import Store, UserProfile, Review

from .serializers import StoreSerializer, UserSerializer, ReviewSerializer

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class StoreList(ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class UserList(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

class ReviewList(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer