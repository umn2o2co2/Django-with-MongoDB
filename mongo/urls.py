from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^read/$', views.read, name='read'),
    url(r'^create/$', views.create, name='create'),
    url(r'^update/$', views.update, name='update'),
    url(r'^delete/$', views.delete, name='delete')
]
