import random
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, ListView

from .models import Office

def office_list_view(request):
    template_name = 'offices/office_list.html'
    query_set = Office.objects.all()
    context = {
        'object_list': query_set
    }
    return render(request, template_name, context)

class OfficeListView(ListView):
    # queryset = Office.objects.all()
    # template_name = 'offices/office_list.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Office.objects.filter(
                Q(country__iexact=slug) |
                Q(country__icontains=slug)
            )
        else:
            queryset = Office.objects.all()
        return queryset


