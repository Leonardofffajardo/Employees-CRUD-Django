from django.contrib import admin
from django.urls import path, include
from . import views

app_name='home_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-prueba/', views.PruebaCreateView.as_view()),
    path('add-prueba/', views.FpruebaCreateView.as_view()),
]
