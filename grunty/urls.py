from django.urls import path
from . import views

urlpatterns = [
    path('', views.table, name='table'),
    path('new', views.new_sample, name='new'),
    path('download', views.download_csv, name='download'),
]

