from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<int:number>/', views.calculate_tax, name='calculate_tax'),
    path('taxrate/', views.tax_rate, name='tax_rate'),

]