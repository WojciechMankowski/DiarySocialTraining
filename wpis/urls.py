from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dziennik/', views.dziennik, name='dziennik'),
    path('login/', views.my_login, name='my_login'),
    path('faq/', views.querAnd, name='faq'),
    path('rejestracja/', views.my_register, name='my_register'),
    path('lista/', views.list_obj, name='lista'),
    path('dowland/', views.dowland, name='dow'),
    path('logout/', views.my_logout, name='logout'),
]