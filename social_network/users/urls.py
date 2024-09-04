from django.urls import path
from .views import UserSignupView, login_view, UserSearchView, send_friend_request, respond_friend_request, list_friends, list_pending_requests

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', login_view, name='login'),
    path('search/', UserSearchView.as_view(), name='search_users'),
    path('friend-request/', send_friend_request, name='send_friend_request'),
    path('friend-request/<int:request_id>/', respond_friend_request, name='respond_friend_request'),
    path('friends/', list_friends, name='list_friends'),
    path('pending-requests/', list_pending_requests, name='list_pending_requests'),
]
