from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import RegisterView, SigninView

urlpatterns = [
    path('sign_up/', RegisterView.as_view(), name='sign-up'),
    path('login/', SigninView.as_view(), name='log-in'),
    path('logout/', LogoutView.as_view(), name='log-out'),
]