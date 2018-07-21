import random
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, ListView, DetailView

from .models import Office


def office_list_view(request):
    template_name = 'offices/office_list.html'
    query_set = Office.objects.all()
    context = {
        'object_list': query_set
    }
    return render(request, template_name, context)


class OfficeListView(ListView):
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


class OfficeDetailView(DetailView):
    queryset = Office.objects.all()

    # def get_object(self, *args, **kwargs):
    #     off_id = self.kwargs.get('off_id')
    #     obj = get_object_or_404(Office, id=off_id) # pk = off_id
    #     return obj
