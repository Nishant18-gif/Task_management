from django.urls import path
from .views import SignupView, LoginView, update_email

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path('update-email/', update_email),
]