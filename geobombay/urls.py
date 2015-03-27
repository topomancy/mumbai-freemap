from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.site_title = 'Mumbai Freemap'
admin.site.site_header = 'Mumbai Freemap'
admin.site.index_title = 'Mumbai Freemap'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geobombay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
