from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from User.views import UserRegistration

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', UserRegistration.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
