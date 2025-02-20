from django.urls import path
from . import views

urlpatterns = [
    path('', views.youtube_stats_view, name='home'),  # Root URL points to the template
    path('youtube-stats/', views.youtube_stats_view, name='youtube_stats'),
]
