import random
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, DetailView, CreateView , ListView
# from django.views.generic.list import ListView

from .forms import ProspectCreateForm, ProspectModelCreateForm
from .models import Prospect


def prospect_create_view(request):
    form = ProspectModelCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/prospects/")

    if form.errors:
        errors = form.errors

    template_name = 'offices/prospect_form.html'
    context = {'form': form, 'errors': errors}
    return render(request, template_name, context)


def office_list_view(request):
    template_name = 'offices/office_list.html'
    query_set = Prospect.objects.all()
    context = {
        'object_list': query_set
    }
    return render(request, template_name, context)


class OfficeListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        print("slug::", slug)
        if slug:
            queryset = Prospect.objects.filter(
                    Q(city__iexact=slug) |
                    Q(city__icontains=slug)
            )
        else:
            queryset = Prospect.objects.all()
            # queryset = Prospect.objects.all().delete()
        return queryset


class OfficeDetailView(DetailView):
    queryset = Prospect.objects.all()  # filter(country__iexact='USA')

    # def get_object(self, *args, **kwargs):
    #     off_id = self.kwargs.get('off_id')
    #     obj = get_object_or_404(Office, id=off_id) # pk = off_id
    #     return obj


class ProspectCreateView(CreateView):
    form_class = ProspectModelCreateForm
    template_name = 'offices/prospect_form.html'
    success_url = "/prospects/"
