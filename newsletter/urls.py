from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('newsletters/', views.newsletter_list, name='newsletter_list'),
]

