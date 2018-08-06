from django.conf.urls import url
from . import views

app_name = 'dobjects'

urlpatterns = [
    url(
        r'^digitalcontainers/$',
        views.DigitalContainerListView.as_view(),
        name='browse_digitalcontainers'
    ),
    url(r'^digitalcontainer/detail/(?P<pk>[0-9]+)$', views.DigitalContainerDetailView.as_view(),
        name='digitalcontainer_detail'),
    url(r'^digitalcontainer/create/$', views.DigitalContainerCreate.as_view(),
        name='digitalcontainer_create'),
    url(r'^digitalcontainer/edit/(?P<pk>[0-9]+)$', views.DigitalContainerUpdate.as_view(),
        name='digitalcontainer_edit'),
    url(r'^digitalcontainer/delete/(?P<pk>[0-9]+)$', views.DigitalContainerDelete.as_view(),
        name='digitalcontainer_delete'),
    url(r'^periods/$', views.PeriodListView.as_view(), name='browse_periods'),
    url(r'^period/detail/(?P<pk>[0-9]+)$', views.PeriodDetailView.as_view(),
        name='period_detail'),
    url(r'^period/create/$', views.PeriodCreate.as_view(),
        name='period_create'),
    url(r'^period/edit/(?P<pk>[0-9]+)$', views.PeriodUpdate.as_view(),
        name='period_edit'),
    url(r'^period/delete/(?P<pk>[0-9]+)$', views.PeriodDelete.as_view(),
        name='period_delete'),
    url(r'^threeds/$', views.ThreeDListView.as_view(), name='browse_threeds'),
    url(r'^threed/detail/(?P<pk>[0-9]+)$', views.ThreeDDetailView.as_view(),
        name='threed_detail'),
    url(r'^threed/create/$', views.ThreeDCreate.as_view(),
        name='threed_create'),
    url(r'^threed/edit/(?P<pk>[0-9]+)$', views.ThreeDUpdate.as_view(),
        name='threed_edit'),
    url(r'^threed/delete/(?P<pk>[0-9]+)$', views.ThreeDDelete.as_view(),
        name='threed_delete'),
    url(r'^photos/$', views.PhotoListView.as_view(), name='browse_photos'),
    url(r'^photo/detail/(?P<pk>[0-9]+)$', views.PhotoDetailView.as_view(),
        name='photo_detail'),
    url(r'^photo/create/$', views.PhotoCreate.as_view(),
        name='photo_create'),
    url(r'^photo/edit/(?P<pk>[0-9]+)$', views.PhotoUpdate.as_view(),
        name='photo_edit'),
    url(r'^photo/delete/(?P<pk>[0-9]+)$', views.PhotoDelete.as_view(),
        name='photo_delete'),
]
