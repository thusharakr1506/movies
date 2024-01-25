"""
URL configuration for imdbapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("movies/all/",views.MovieListView.as_view(),name="movie-list"),
    path("movies/<int:pk>/",views.MovieDetailView.as_view(),name="movie-detail"),
    path("movies/<int:pk>/remove/",views.MovieDeleteView.as_view(),name="movie-delete"),
    path("movies/add/",views.MovieCreateView.as_view(),name="movie-add"),
    path("movies/<int:pk>/change/",views.MovieUpdateView.as_view(),name="movie-edit"),

]
