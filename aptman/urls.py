from django.urls import path

from . import views

app_name = 'aptman'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:apt_id>/', views.details, name='details'),
    path('add-apartment/', views.add_apartment, name='addapt'),
    path('add-tenant/', views.add_tenant, name='addtenant'),
    path('edit-apartment/<int:apt_id>/', views.edit_apt, name='editapt'),
    path('vacant-apartments', views.view_vacant, name='vacant-apartments')
]