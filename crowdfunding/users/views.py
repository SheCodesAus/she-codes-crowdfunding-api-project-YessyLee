from django.http import Http404
from projects.permissions import IsOwnProfile
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .models import CustomUser
from .serializers import CustomUserSerializer, ChangePasswordSerializer, CustomUserDetail

# Create your views here.
class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def post(self, request):
        if request.user.is_authenticated:
            return Response({"error": "You cannot create a new user while you are logged in."})
        else:
            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                if 'email' in serializer.errors:
                    return Response({"error":"This email is associated with another user. Please login or choose an alternative email."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(
                        serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    
class CustomUserDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnProfile]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetail
    
    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response(
                {"data": "Sorry, you don't have access to this page!"}, status=status.HTTP_404_NOT_FOUND
            )
        return super(CustomUserDetailView, self).handle_exception(exc)
    
# class CustomUserList(APIView):
# 
    # def get(self, request):
        # users = CustomUser.objects.all()
        # serializer = CustomUserSerializer(users, many=True)
        # return Response(serializer.data)
# 
    # def post(self, request):
        # serializer = CustomUserSerializer(data=request.data)
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data)
        # return Response(serializer.errors)
    # 
# class CustomUserDetail(APIView):
    # permission_classes = [IsAuthenticated,]
# 
    # def get_object(self, pk):
        # try:
            # return CustomUser.objects.get(pk=pk)
        # except CustomUser.DoesNotExist:
            # raise Http404
# 
    # def get(self, request, pk):
        # user = self.get_object(pk)
        # serializer = CustomUserSerializer(user)
        # return Response(serializer.data)
    # 

#Code inspo from https://studygyaan.com/django/django-rest-framework-tutorial-change-password-and-reset-password    
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = CustomUser
    permission_classes = (IsAuthenticated,)

    #ensuring the right user logged in first
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    #get the display work properly on the screen/url
    def get(self, request, *args, **kwargs):
        return Response({"message":f"Ok, let's change your password {self.request.user.username}"})

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        