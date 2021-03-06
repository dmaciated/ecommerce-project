from django.conf.urls import patterns, include, url
from django.contrib import admin

from rides import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freerides.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^rides/', include('rides.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
)
