from django.urls import path

from . import views

app_name = 'aptman'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:apt_id>/', views.details, name='details'),
    path('add-apartment/', views.add_apartment, name='addapt'),
    path('add-tenant/', views.add_tenant, name='addtenant'),
    path('edit-apartment/<int:apt_id>/', views.edit_apt, name='editapt'),
    path('edit-tenant/<int:tenant_id>/', views.edit_tenant, name='edit-tenant'),
    path('flag-late/', views.flag_late, name='flag-late'),
    path('tenant-history/<int:tenant_id>/', views.view_history, name='tenant-history'),
    path('to-evict/', views.to_evict, name='to-evict'),
    path('update-history/', views.update_history, name='update-history'),
    path('vacant-apartments/', views.view_vacant, name='vacant-apartments'),
    path('view-tenants/', views.view_tenants, name='view-tenants')
]