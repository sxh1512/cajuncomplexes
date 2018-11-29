from django.urls import path

from . import views

app_name = 'aptman'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:apt_id>/', views.details, name='details')
]