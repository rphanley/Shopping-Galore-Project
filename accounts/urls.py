from django.conf.urls import url, include
from accounts import urls_reset
from .views import index, register, profile, logout, login
from products.views import all_products


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^products/$', all_products, name='products'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]
