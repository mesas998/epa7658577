from django.conf.urls import url

from ..views import NutDataDetail, nutdata_list, NutDataCreate

urlpatterns = [
    #rl(r'^$', nutdata_list, name='nutr_nutdata_list'),
    url(r'^$', nutdata_list),
    url(r'^create/$', NutDataCreate.as_view(), name='nutr_nutdata_create'),
    url(r'^(?P<pk>\d)/$', NutDataDetail.as_view(), name='nutr_nutdata_detail'),
]
