from django.http import HttpResponse, Http404
from django.shortcuts import render

def inicio(request):	
	return render (request, 'index.html')

def about(request):
	texto = "Proyecto de Indicadores (KPIs) -  Sergio Alexander Gutierrez - CodeTag"
	return render (request, 'about.html', {'texto': texto})