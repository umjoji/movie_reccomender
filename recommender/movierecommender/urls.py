from django.urls import path, include
from . import views
import django.contrib.auth.urls


urlpatterns = [
    # route is a string contains a URL pattern
    path(route='', view=views.movie_recommendation_view, name='recommendations'), # type: ignore
    # path('register/', views.register_request, name='register'),
    path('api/', views.MovieListApiView.as_view(), name='api_view'),
    # path('api/<str:pk>/', views.api_detail_view, name='api_detail'),

]
