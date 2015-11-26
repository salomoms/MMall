from django.conf.urls import include, url, patterns
from django.contrib import admin
from MMall import settings
from ecommerce.views import index, addToCart, cart, checkout

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls), name='index'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^cart/add/(?P<id>[0-9]+)/(?P<slug>.*)$', addToCart, name='add_to_cart'),
    url(r'^cart', cart, name='cart'),
    url(r'^checkout', checkout, name='checkout'),
]


# Debug Toolbar :D
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )