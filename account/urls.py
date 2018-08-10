from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import LoginView, CreateUserView, DashboardView, LogoutView

app_name = 'account'

urlpatterns = [
    path('auth/token/', obtain_auth_token, name='get_jwt'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard')
]