from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practica5.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^help', 'P5.views.help', name='help'),
    url(r'^home', 'P5.views.home', name='home'),
    url(r'^about', 'P5.views.about', name='about'),
)
