from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
# from .serializers import UserSerializer ,CarDetailSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# from .models import CarDetail
from rest_framework_simplejwt.tokens import RefreshToken



@method_decorator(csrf_exempt, name='dispatch')
class SignUpAPI(APIView):
    def post(self, request):
        uname = request.data.get('username')
        uemail = request.data.get('email')
        pass1 = request.data.get('password')
        pass2 =  pass1
        if pass1 != pass2:
            return Response({'error': 'Password not matching'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if User.objects.filter(username=uname).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(email=uemail).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            my_user = User.objects.create_user(uname, uemail, pass1)
            my_user.save()
            return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)
        

class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        # generate token

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = CustomAccessToken.for_user(user)
            return Response({'message': 'Login successful',
                             'access': str(refresh.access_token),
                             'refresh': str(refresh)
                             }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)




class CustomAccessToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        token = super().for_user(user)
        token['username'] = user.username
        token['id'] = user.id
        token['email'] = user.email
        return token