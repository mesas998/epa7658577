from django.conf.urls import url

from ..views import epacolo_list

urlpatterns = [
    #rl(r'^$', epacolo_list, name='nutr_epacolo_list'),
    url(r'^$', epacolo_list),
    #rl(r'^create/$', EPAColoCreate.as_view(), name='nutr_epacolo_create'),
    #rl(r'^(?P<slug>[\w\-]+)/delete/$', EPAColoDelete.as_view(), name='nutr_epacolo_delete'),
    #rl(r'^(?P<slug>[\w\-]+)/update/$', EPAColoUpdate.as_view(), name='nutr_epacolo_update'),
    #rl(r'^(?P<slug>[\w]+)/$', EPAColoDetail.as_view(), name='nutr_epacolo_detail'),
]

