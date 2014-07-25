from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import KPIs.settings
import django
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from indicadores.forms import *
import simplejson
from indicadores.models import *
from django.http import HttpResponseRedirect

def addIndicador(request):
	info = "Inicializando" 
	if request.method == "POST":
		form = addIndicadorForm(request.POST)
		if form.is_valid():
			add = form.save(commit=False) 
			add.status = True
			add.save() #Guarda la informacion
			form.save_m2m() # guarda las relaciones de ManyToMany
			info = "Se guardo satisfactoriamente!!!!!"
			return HttpResponseRedirect('/indicador/insertar/')
	else:
		form = addIndicadorForm()
	ctx = {'form':form, 'informacion':info}
	return render_to_response('indicador/insertar.html',ctx,context_instance=RequestContext(request))

def indicadores_view(request,pagina):
	if request.method=="POST":
		if "indicador_id" in request.POST:
			try:
				id_indicador = request.POST['indicador_id']
				p = Indicador.objects.get(pk=id_indicador)
				mensaje = {"status":"True","indicador_id":p.id}
				p.delete() # Elinamos objeto de la base de datos
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"status":"False"}
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
	lista_indicador = Indicador.objects.all() # Select * from ventas_productos where status = True
	paginator = Paginator(lista_indicador,5)# Cuantos productos quieres por pagina? = 3
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		indicadores = paginator.page(page)
	except (EmptyPage,InvalidPage):
		indicadores= paginator.page(paginator.num_pages)
	ctx = {'indicadores':indicadores, 'lista':lista_indicador}
	return render_to_response('indicador/indicadores.html',ctx,context_instance=RequestContext(request))