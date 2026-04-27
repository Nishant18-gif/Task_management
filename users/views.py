from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .models import CustomUser
from .serializers import UserSerializer


# Signup API
class SignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# Login API
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })

        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


#  Update Email API
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_email(request):
    user = request.user
    user.email = request.data.get('email')
    user.save()
    return Response({"message": "Email updated"})


#  change password 
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_password(request):
    user = request.user

    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')

    if not old_password or not new_password:
        return Response({"error": "Both old and new password are required"}, status=400)

    if not user.check_password(old_password):
        return Response({"error": "Old password incorrect"}, status=400)

    if len(new_password) < 6:
        return Response({"error": "Password must be at least 6 characters"}, status=400)

    if user.check_password(new_password):
        return Response({"error": "New password cannot be same as old password"}, status=400)

    user.set_password(new_password)
    user.save()

    return Response({"message": "Password updated successfully"})