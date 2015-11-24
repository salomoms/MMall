from django.conf.urls import include, url, patterns
from django.contrib import admin
from MMall import settings
from ecommerce.views import index

urlpatterns = [
    url(r'^', index),
    url(r'^admin/', include(admin.site.urls), name='index'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]


# Debug Toolbar :D
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )