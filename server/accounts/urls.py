from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView 

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(),name="login"),
    path('signup/', views.SignUpView.as_view(),name="signup"),

    path('jwt/create/', TokenObtainPairView.as_view(), name="jwt-create"),
    path('jwt/refresh/', TokenRefreshView.as_view(), name="jwt-refresh"),
    path('jwt/verify/', TokenVerifyView.as_view(), name="jwt-verify")
]