from django.conf.urls import url

from ..views import nutrdef_detail, nutrdef_list, NutrDefDetail, NutrDefCreate, NutrDefDelete, NutrDefUpdate, NutDataCreate

urlpatterns = [
    #rl(r'^$', nutrdef_list, name='nutr_nutrdef_list'),
    url(r'^$', nutrdef_list),
    url(r'^create/$', NutrDefCreate.as_view(), name='nutr_nutrdef_create'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', NutrDefDelete.as_view(), name='nutr_nutrdef_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$', NutrDefUpdate.as_view(), name='nutr_nutrdef_update'),
    url(r'^(?P<slug>[\w]+)/$', NutrDefDetail.as_view(), name='nutr_nutrdef_detail'),
]

