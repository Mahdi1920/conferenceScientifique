from django.urls import path
from .views import SessionDetailView, SessionListView, about, home, profile


urlpatterns = [
    path('home/', home, name='session_home'),
    path('about/', about, name='session_about'),
    path('profile/<str:username>/', profile, name='session_profile'),
    path('sessionsLV/', SessionListView.as_view(), name='session_lv'),
    path('session/<int:pk>/', SessionDetailView.as_view(), name='session_detail_lv'),
]