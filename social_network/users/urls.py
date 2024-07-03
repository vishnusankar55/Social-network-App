# users/urls.py

from django.urls import path
from .views import SignupView, LoginView, UserSearchView, FriendRequestView, AcceptFriendRequestView, FriendListView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friend-requests/', FriendRequestView.as_view(), name='friend-requests'),
    path('friend-requests/<int:pk>/accept/', AcceptFriendRequestView.as_view(), name='accept-friend-request'),
    path('friends/', FriendListView.as_view(), name='friends-list'),
]
