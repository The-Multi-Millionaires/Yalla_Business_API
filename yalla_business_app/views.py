from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



from .forms import CustomUserCreationForm

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework import filters


from .models import Store, UserProfile, Review, CustomUser

from .serializers import StoreSerializer, UserSerializer, ReviewSerializer, CostumUserSerializer

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class StoreList(ListCreateAPIView):
    search_fields = ['store_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    # def get_queryset(self):
    #     return Review.objects.filter(user=self.kwargs['store_id'])

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


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class ReviewList(ListCreateAPIView):
    # search_fields = ['store_id__id']
    filter_backends = (DynamicSearchFilter,)
    # filter_backends = (filters.SearchFilter,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class Users(ListCreateAPIView):
    search_fields = ['username']
    filter_backends = (filters.SearchFilter,)
    queryset = CustomUser.objects.all()
    serializer_class = CostumUserSerializer

class UsersDetails(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CostumUserSerializer
