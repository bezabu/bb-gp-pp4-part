from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dash_list'),
    path('defect_list/<int:page>/', views.defect_list, name='def_list'),
    path('category_list/', views.category_list, name='cat_list'),
    path('dashboard/', views.dashboard, name='dash_list'),
    path('log_defect/', views.log_defect, name='log_def'),
    path('<int:defect_id>/', views.defect_detail, name='def_detail'),
    path(
        '<int:defect_id>/edit_update/<str:update_id>',
        views.update_edit, name='upd_edit'),
    path(
        '<int:defect_id>/delete_update/<str:update_id>',
        views.update_delete, name='upd_delete'),
]
