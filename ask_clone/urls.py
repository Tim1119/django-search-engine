from django.urls import path
from .views import HomeView,ResultView

app_name='clone'

urlpatterns = [
    path('',HomeView,name='home'),
    path('results/',ResultView,name='result')
]
