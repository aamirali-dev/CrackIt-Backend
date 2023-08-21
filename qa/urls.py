from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('qa/<str:category>', views.questions),
    path('categories/', views.categories)
]