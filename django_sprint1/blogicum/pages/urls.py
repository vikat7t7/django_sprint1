from django.urls import path
from . import views

urlpatterns = [
    path('pages/about/', views.about),
    path('pages/rules/', views.rules),
]
