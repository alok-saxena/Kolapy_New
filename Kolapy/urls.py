from django.conf.urls import patterns, url
from Kolapy_Django import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
      url(r'^$', views.home),
      url(r'^stocks/([A-Z]*)', views.stocks)
    # url(r'^Kolapy/', include('Kolapy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
