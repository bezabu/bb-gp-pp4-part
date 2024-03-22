from . import views
from django.urls import path

urlpatterns = [
    path('defect_list/', views.defect_list, name='def_list'),
    path('category_list/', views.CategoryList.as_view(), name='cat_list'),
    path('dashboard/', views.DashList.as_view(), name='dash_list'),
]