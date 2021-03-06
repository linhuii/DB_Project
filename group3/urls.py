from django.conf.urls import patterns, include, url
from group3 import views

urlpatterns = patterns('',
    url(r'/currentuser/$', views.exampleCurrentUser, name='example_currentuser'),
    url(r'^prof2lang/$', views.prof2lang_index, name='prof2lang_index'),
    url(r'^prof2lang/(\d+)/$', views.prof2lang_view, name='prof2lang_view'),
    url(r'^prof2lang/add/(\d+)$', views.prof2lang_add, name='prof2lang_add'),
    url(r'^addProf/$', views.addProf, name='addProf'),
    url(r'^addSubject/$', views.addSubject, name='addSubject'),
    url(r'^addSection/$', views.addSection, name='addSection'),
    url(r'^testpdf/(\d+)/$', views.genpdf, name='genpdf'),
    url(r'^genallpdf/$', views.genallpdf, name='genallpdf'),
    url(r'^hourpdf/$', views.hourpdf, name='hourpdf'),
    url(r'^prof2lang/delete/(\d+)$', views.prof2lang_delete, name='prof2lang_delete'),
)
