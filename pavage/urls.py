from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('charger', views.charger, name='charger'),
    path('pavage_reponse',views.pavage_reponse,name='pavage_reponse'),
]

