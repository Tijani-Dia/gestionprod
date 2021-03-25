from django.urls import path, include

from . import views

app_name = 'suivichargement'

urlpatterns = [
    path('', views.index, name='index'),
    path('consulter/<slug:parametre>/', views.consult , name='consult'),
    path('soumettre/<slug:parametre>/', views.submit , name='submit'),
]