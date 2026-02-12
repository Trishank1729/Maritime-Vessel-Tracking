from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    api_root,
    CustomTokenObtainPairView,
    register,
    profile,
    update_profile,
    user_list,
    user_detail,
    get_user_stats,
)

app_name = 'api'

urlpatterns = [
    # API Root
    path('', api_root, name='api_root'),
    
    # Authentication
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register'),
    
    # User Profile
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    
    # User Management
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('stats/', get_user_stats, name='user_stats'),
]
