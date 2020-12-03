from django.urls import path
from . import views

urlpatterns = [
 path('home', views.home, name='home'),
 path('', views.index, name='index'),
 path('departamento/<int:departamento_id>', views.detail, name='detail'),
 path('departamento/<int:departamento_id>/empleados', views.empleados, name='empleados'),
 path('empleado/<int:empleado_id>', views.empleado, name='empleado'),
 path('habilidad/<int:habilidad_id>', views.habilidad, name='habilidad')
]