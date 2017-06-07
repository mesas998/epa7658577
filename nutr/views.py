from django.core.urlresolvers import reverse_lazy
from django.shortcuts import ( get_object_or_404, redirect, render)

from django.shortcuts import get_object_or_404
from django.views.generic import ( CreateView, DeleteView, DetailView, ListView)

#rom .forms import ( NewsLinkForm, NutDataForm, TagForm)
#rom .models import NewsLink, NutData, Tag
from .utils import ( PageLinksMixin, NutDataContextMixin)

from django.http.response import HttpResponse
from django.template import Context, loader

from .models import NutrDef, NutData, EPAColo
from .utils import ( PageLinksMixin, NutDataContextMixin)
from .forms import NutrDefForm, NutDataForm
from django.views.generic import ( CreateView, DeleteView, DetailView, ListView)
from core.utils import UpdateView
from user.decorators import class_login_required, require_authenticated_permission
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator


def homepage(request):
    nutrdef_list = NutrDef.objects.all()
    template = loader.get_template(
        'nutr/nutrdef_list.html')
    #ontext = Context({'nutrdef_list': nutrdef_list})
    context={'nutrdef_list': nutrdef_list}
    output = template.render(context)
    return HttpResponse(output)

def nutrdef_detail(request, pk):
    #utrdef = get_object_or_404( NutrDef, nutr_no__iexact=nutr_no)
    #eturn render( request, 'nutr/nutr_detail.html', {'nutrdef': nutrdef})
    #utrdef = NutrDef.objects.get(nutr_no__iexact=nutr_no)
    nutrdef = NutrDef.objects.get(pk=pk)
    template = loader.get_template(
        'nutr/nutrdef_detail.html')
    #ontext = Context({'nutrdef': nutrdef})
    context = {'nutrdef': nutrdef}
    return HttpResponse(template.render(context))

def nutrdef_list(request):
    return render(
        request,
        'nutr/nutrdef_list.html',
        {'nutrdef_list': NutrDef.objects.all()})

class NutDataDetail(DetailView):
    model = NutData

class NutrDefDetail(DetailView):
    model = NutrDef

#lass NutDataList(PageLinksMixin, ListView):
    #odel = NutData
    #aginate_by = 5  # 5 items per page
def nutdata_list(request):
    return render(
        request,
        'nutr/nutdata_list.html',
        {'nutdata_list': NutData.objects.all()})


#require_authenticated_permission(
    #nutr.add_nutrdef')
class NutrDefCreate(CreateView):
    form_class = NutrDefForm
    model = NutrDef


#require_authenticated_permission(
    #nutr.delete_nutrdef')
class NutrDefDelete(DeleteView):
    model = NutrDef
    success_url = reverse_lazy(
        'nutr_nutrdef_list')

#require_authenticated_permission(
    #nutr.change_nutrdef')
class NutrDefUpdate(UpdateView):
    form_class = NutrDefForm
    model = NutrDef

#require_authenticated_permission(
    #nutr.add_nutdata')
class NutDataCreate(CreateView):
    form_class = NutDataForm

def epacolo_list(request):
    return render(
        request,
        'nutr/epacolo_list.html',
        {'epacolo_list': EPAColo.objects.all()})

