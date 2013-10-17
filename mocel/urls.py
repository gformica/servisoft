from django.conf.urls import patterns, url

from mocel import views

urlpatterns = patterns(
	'',
	url(r'^index/$', views.index, name='index'),
	url(r'^login/$', views.login),
	url(r'^logout/$', views.logout),
)
