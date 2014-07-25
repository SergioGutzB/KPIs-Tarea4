from django.conf.urls import patterns, include, url

urlpatterns = patterns( 'indicadores.views',
	url(r'^insertar/$', 'addIndicador', name='insertar'),
    url(r'^page/(?P<pagina>.*)/$', 'indicadores_view', name='indicadores'),
)
