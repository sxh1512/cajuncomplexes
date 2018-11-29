from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:apt_id>/', views.details, name='details')
]