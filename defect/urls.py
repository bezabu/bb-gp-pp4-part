from . import views
from django.urls import path

urlpatterns = [
    path('defect_list/', views.defect_list, name='def_list'),
    path('category_list/', views.category_list, name='cat_list'),
    path('dashboard/', views.dashboard, name='dash_list'),
    path('log_defect/', views.log_defect, name='log_def'),
    path('<defect_id>/', views.defect_detail, name='def_detail'),
    path('', views.dashboard, name='dash_list'),
]