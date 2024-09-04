from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.pagination import PageNumberPagination
from .models import User, FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer

class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email.lower(), password=password)
    if user:
        return Response(UserSerializer(user).data)
    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        search_keyword = self.request.query_params.get('q', '').lower()
        if '@' in search_keyword:
            return User.objects.filter(email__iexact=search_keyword)
        return User.objects.filter(username__icontains=search_keyword)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_friend_request(request):
    to_user_id = request.data.get('to_user')
    to_user = User.objects.get(id=to_user_id)
    FriendRequest.objects.create(from_user=request.user, to_user=to_user, status='pending')
    return Response({"message": "Friend request sent"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def respond_friend_request(request, request_id):
    friend_request = FriendRequest.objects.get(id=request_id)
    status = request.data.get('status')
    if status in ['accepted', 'rejected']:
        friend_request.status = status
        friend_request.save()
        return Response({"message": f"Friend request {status}"})
    return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_friends(request):
    friends = FriendRequest.objects.filter(from_user=request.user, status='accepted')
    serializer = FriendRequestSerializer(friends, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_pending_requests(request):
    pending_requests = FriendRequest.objects.filter(to_user=request.user, status='pending')
    serializer = FriendRequestSerializer(pending_requests, many=True)
    return Response(serializer.data)
