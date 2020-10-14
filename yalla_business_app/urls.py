from django.urls import path
from .views import SignUpView,StoreDetails

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/', StoreDetails.as_view(), name='store_details') 
]