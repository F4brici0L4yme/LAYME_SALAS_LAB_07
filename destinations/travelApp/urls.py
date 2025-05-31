from django.urls import path

from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('listar/', views.listar_destinos, name='listar_destinos'),
    path('agregar/', views.agregar_destino, name='agregar_destino'),
    path('editar/<int:pk>/', views.editar_destino, name='editar_destino'),
    path('eliminar/<int:pk>/', views.eliminar_destino, name='eliminar_destino'),
    path("", views.index, name="index")
]
