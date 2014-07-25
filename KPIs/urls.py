from django.conf.urls import patterns, include, url
import settings
from django.conf.urls.static import static
import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KPIs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^about/', 'KPIs.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^indicador/', include ('indicadores.urls')),
    url(r'^$', 'KPIs.views.inicio', name='index'),
)