from django.urls import path
from users.views import UserView, UserGetIdView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserGetIdView.as_view()),
]
