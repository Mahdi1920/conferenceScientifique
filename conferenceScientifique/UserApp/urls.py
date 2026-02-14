from django.urls import path
from .views import UserListView, UserDetailView, about, home, profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', home, name='user_home'),
    path('about/', about, name='user_about'),
    path('profile/<str:username>/', profile, name='user_profile'),
    path('usersLV/', UserListView.as_view(), name='user_lv'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail_lv'),
    path('login/', auth_views.LoginView.as_view(template_name='User/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),    
]