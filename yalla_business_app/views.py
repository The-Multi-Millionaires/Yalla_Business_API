from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# from django.shortcuts import render
from rest_framework import generics

from .models import StoreProfile
from .serializer import StoreSerializer

class StoresList(generics.ListCreateAPIView):
    queryset = StoreProfile.objects.all()
    serializer_class = StoreSerializer

class StoreDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreProfile.objects.all()
    serializer_class = StoreSerializer