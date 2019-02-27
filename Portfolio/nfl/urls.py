from django.urls import path
from . import views

app_name = 'nfl'

urlpatterns = [
    path('nfl_index', views.NflIndexView.as_view(), name='nfl_index')
]
