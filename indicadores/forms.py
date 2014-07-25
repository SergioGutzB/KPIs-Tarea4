from django import forms
from django.contrib.auth.models import User
from indicadores.models import *


class IndicadorForm(forms.Form):
	Nombre	= forms.CharField(widget=forms.TextInput())
	Descripcion_Concepto	= forms.CharField(widget=forms.Textarea())
	Descripcion_Operacion	= forms.CharField(widget=forms.Textarea())
	Otro = forms.CharField(widget=forms.Textarea())

class addIndicadorForm(forms.ModelForm):
	class Meta:
		model = Indicador
		exclude = {'status', }