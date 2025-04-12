from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('newsletters/', views.newsletter_list, name='newsletter_list'),
    path('subscribe/success/', views.subscribe_success, name='subscribe_success'),  # noqa:E501
]
