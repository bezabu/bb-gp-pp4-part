from . import views
from django.urls import path

urlpatterns = [
    path('defect_list/', views.DefectList.as_view(), name='def_list'),
    path('category_list/', views.CategoryList.as_view(), name='cat_list'),
]