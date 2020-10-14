from django.urls import path
from .views import SignUpView, StoreList, UserList, ReviewList


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', StoreList.as_view(), name='storelist'),
    path('userprofile/', UserList.as_view(), name='userlist'),
    path('review/', ReviewList.as_view(), name='review'),

]