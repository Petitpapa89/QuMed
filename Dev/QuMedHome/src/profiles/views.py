import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, ListView

from .models import Office

def office_list_view(request):
    template_name = 'offices/offices_list.html'
    query_set = Office.objects.all()
    context = {
        'object_list': query_set
    }
    return render(request, template_name, context)

class OfficeListView(ListView):
    queryset = Office.objects.all()
    template_name = 'offices/offices_list.html'


class USOfficeListView(ListView):
    queryset = Office.objects.filter(country__iexact="usa")
    template_name = 'offices/offices_list.html'

class ForeignOfficeListView(ListView):
    queryset = Office.objects.exclude(country__iexact="usa")
    template_name = 'offices/offices_list.html'

