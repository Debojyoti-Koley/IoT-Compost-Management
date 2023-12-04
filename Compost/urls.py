from django.urls import path
from .views import home, timelyUpdate, alerts, add_compost
urlpatterns = [
    path('', home, name='home'),
    path('timelyUpdate/', timelyUpdate),
    path('add_compost/', add_compost, name='add_compost'),
    path('alert/', alerts),
]