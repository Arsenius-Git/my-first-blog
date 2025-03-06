from django.urls import path
from . import views

urlpatterns = [
    path("", views.weather, name="weather"),
    path("weather/", views.view_weather, name='view_weather'),
    path("todo/", views.view_todo, name='view_todo'),
    path("create/", views.create, name='create'),
    path("url/", views.short_url, name='short_url'),
    path("expenses/", views.expenses_track, name='expense_track'),
]