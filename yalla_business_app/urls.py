from django.urls import path
from .views import SignUpView, StoreList, UserList, ReviewList, StoreDetails, ProfileDetails,ReviewDetails


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('api/v1/stores', StoreList.as_view(), name='storelist'),
    path('api/v1/stores/<int:pk>/',StoreDetails.as_view(),name='storedetails'),

    path('api/v1/userprofile/', UserList.as_view(), name='userlist'),
    path('api/v1/userprofile/<int:pk>/',ProfileDetails.as_view(),name='userdetails'),

    path('api/v1/review/', ReviewList.as_view(), name='review'),
    path('api/v1/review/<int:pk>/',ReviewDetails.as_view(),name='reviewdetails'),

]