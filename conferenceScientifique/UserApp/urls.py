from django.urls import path
from .views import UserListView, UserDetailView, about, home, profile


urlpatterns = [
    path('home/', home, name='user_home'),
    path('about/', about, name='user_about'),
    path('profile/<str:username>/', profile, name='user_profile'),
    path('usersLV/', UserListView.as_view(), name='user_lv'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail_lv'),
]