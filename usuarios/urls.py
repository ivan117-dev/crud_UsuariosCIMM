#urls.py (usuarios)
from django.urls import path
from usuarios import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.usuario_list, name='usuario_list'),
    path('new/', views.create_usuario, name='create_usuario'),
    path('edit/<int:pk>/', views.update_usuario, name='update_usuario'),
    path('delete/<int:pk>/', views.delete_usuario, name='delete_usuario'),
    path('pdf',views.generar_pdf_usuario , name='generar_pdf_usario'),

    #Rutas para login
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register')
]