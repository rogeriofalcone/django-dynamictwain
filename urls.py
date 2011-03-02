from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'scan/$', 'dynamictwain.views.scan', name='scan'),
    url(r'form/$', 'dynamictwain.views.form', name='form'),
    url(r'redirect/$', 'dynamictwain.views.redirect', name='redirect'),
    url(r'upload/$', 'dynamictwain.views.upload', name='upload'),
)
