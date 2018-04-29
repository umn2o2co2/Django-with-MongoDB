from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^read/$', views.ReadListView.as_view(), name='read'),
    url(r'^create/$', views.CreateObjectView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.UpdateObjectView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteObjectView.as_view(), name='delete'),
    url(r'^details/(?P<pk>\d+)/$', views.ObjectDetailView.as_view(), name='details'),
]
