from . import views
from django.urls import path

urlpatterns = [
    path('', views.DefectList.as_view(), name='list'),
]