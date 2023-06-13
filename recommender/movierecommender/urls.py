from django.urls import path, include
from . import views
import django.contrib.auth.urls


urlpatterns = [
    # route is a string contains a URL pattern
    path('register/', views.register_request, name='register'),
    path(route='', view=views.movie_recommendation_view, name='recommendations'), # type: ignore
]
