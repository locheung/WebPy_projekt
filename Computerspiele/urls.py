from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.function_based_view_spiel_list, name='spiel-list'),
    path('show/<int:pk>/', views.function_based_view_spiel_detail, name='spiel-detail'),
    path('show/<int:pk>/delete/', views.function_based_view_spiel_delete, name='spiel-delete'),
    path('add/', views.function_based_view_spiel_create, name='spiel-create'),
]