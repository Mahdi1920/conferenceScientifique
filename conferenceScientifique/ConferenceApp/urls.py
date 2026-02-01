from django.urls import path
from .views import ConferenceDetailView, about, conferenceList, ConferenceListView, home, profile


urlpatterns = [
    path('home/', home, name='conference_home'),
    path('about/', about, name='conference_about'),
    path('profile/<str:username>/', profile, name='conference_profile'),
    path('conferences/', conferenceList, name='conference_list'),
    path('conferencesLV/', ConferenceListView.as_view(), name='conference_lv'),
    path('conference/<int:pk>/', ConferenceDetailView.as_view(), name='conference_detail_lv'),
]