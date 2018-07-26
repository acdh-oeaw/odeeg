from django.conf.urls import url
from . import views

app_name = 'dobjects'

urlpatterns = [
    url(r'^periods/$', views.PeriodListView.as_view(), name='browse_periods'),
    url(r'^period/detail/(?P<pk>[0-9]+)$', views.PeriodDetailView.as_view(),
        name='period_detail'),
    url(r'^period/create/$', views.PeriodCreate.as_view(),
        name='period_create'),
    url(r'^period/edit/(?P<pk>[0-9]+)$', views.PeriodUpdate.as_view(),
        name='period_edit'),
    url(r'^period/delete/(?P<pk>[0-9]+)$', views.PeriodDelete.as_view(),
        name='period_delete'),
]
