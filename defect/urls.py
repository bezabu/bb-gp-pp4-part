from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name='dash_list'),
    path('defect_list/', views.defect_list, name='def_list'),
    path('category_list/', views.category_list, name='cat_list'),
    path('dashboard/', views.dashboard, name='dash_list'),
    path('log_defect/', views.log_defect, name='log_def'),
    path('<int:defect_id>/', views.defect_detail, name='def_detail'),
    path('<int:defect_id>/edit_update/<int:update_id>', views.update_edit, name='update_edit'),
    path('<int:defect_id>/delete_update/<int:update_id>', views.update_delete, name='update_delete'),
]