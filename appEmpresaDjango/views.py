from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Departamento, Habilidad, Empleado
from django.db.models import OuterRef, Subquery, Max

#devuelve el listado de empresas

def home(request):
	departamentos = get_list_or_404(Departamento.objects.order_by('nombre'))
	
	#empleadosFiltrados = Empleado.objects.raw('SELECT * FROM( SELECT * FROM appEmpresaDjango_empleado ORDER BY antiguedad DESC) GROUP BY departamento_id ')
	#empleadosFiltrados = ( Empleado.objects.annotate(max_antiguedad=Max('antiguedad')).order_by('departam7ento_id', '-antiguedad').distinct('departamento_id') )
	
	# Obtener la antigüedad máxima por cada departamento
	max_antiguedad_por_departamento = Empleado.objects.filter(departamento_id=OuterRef('departamento_id')).order_by().values('departamento_id').annotate(max_antiguedad=Max('antiguedad')).values('max_antiguedad')
	# Filtrar empleados que tengan la antigüedad máxima en su departamento
	empleadosFiltrados = Empleado.objects.filter(antiguedad__in=max_antiguedad_por_departamento).order_by('departamento_id', '-antiguedad')

	context = {'empleadosFiltrados': empleadosFiltrados }
	return render(request, 'home.html', context)

def index(request):
	departamentos = get_list_or_404(Departamento.objects.order_by('nombre'))
	context = {'lista_departamentos': departamentos }
	return render(request, 'index.html', context)

#devuelve los datos de un departamento
def detail(request, departamento_id):
	departamento = get_object_or_404(Departamento, pk=departamento_id)
	context = {'departamento': departamento }
	return render(request, 'detail.html', context)

#devuelve los empelados de un departamento
def empleados(request, departamento_id):
	departamento = get_object_or_404(Departamento, pk=departamento_id)
	empleados =  departamento.empleado_set.all()
	context = {'departamento': departamento, 'empleados' : empleados }
	return render(request, 'empleados.html', context)

#devuelve los detalles de un empleado
def empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    habilidades =  empleado.habilidades.all()
    context = { 'empleado': empleado, 'habilidades' : habilidades }
    return render(request, 'empleado.html', context)

# Devuelve los detalles de una habilidad
def habilidad(request, habilidad_id):
    habilidad = get_object_or_404(Habilidad, pk=habilidad_id)
    empleados =  habilidad.empleado_set.all()
    context = { 'empleados': empleados, 'habilidad' : habilidad }
    return render(request, 'habilidad.html', context)