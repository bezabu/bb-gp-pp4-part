from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home'),
    path('defect_list/', views.defect_list, name='def_list'),
    path('category_list/', views.CategoryList.as_view(), name='cat_list'),
    path('dashboard/', views.dashboard, name='dash_list'),
    path('<defect_id>/', views.defect_detail, name='def_detail'),
]