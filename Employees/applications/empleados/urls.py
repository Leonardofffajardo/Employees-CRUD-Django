from django.contrib import admin
from django.urls import path, include
#VIEWS
from . import views

app_name= 'persona_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar-todo-empleados/', views.List_AllempleadosListView.as_view(), name= 'listar_todos'),
    path('listar-area/<shorname>/', views.List_byempleadosListView.as_view(), name='empleados_area'),
    path('listar-trabajos/<jobs>/', views.Byjob_ListView.as_view()),
    path('buscar-empleado/', views.ByKwordListView.as_view()),
    path('habilidades-empleado/', views.Habilidades_empleadosListView.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view()),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='add'),
    path('success/', views.SuccessView.as_view(), name= 'correcto'),
    path('update/<pk>/', views.EmpleadoUpdateView.as_view(), name= 'update'),
    path('delete/<pk>/', views.EmpleadoDeleteView.as_view(), name= 'delete'),
    path('', views.InicioView.as_view(), name= 'inicio'),
    path('detalle/<pk>/', views.Detail_EmpleadoListView.as_view(), name='detail'),
    path('lista-empleados-admin/', views.List_Empleados_admin.as_view(), name='list_admin'),
]
