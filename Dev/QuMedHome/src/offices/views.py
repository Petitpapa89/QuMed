import random
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, ListView, DetailView

from .forms import ProspectCreateForm
from .models import Prospect


def prospect_create_view(request):
    # if request.method == 'GET':
    #     print('get data')

    if request.method == 'POST':
        print('post data')
        print(request.POST)
        first_name = request.POST.get('first_name')  # PUT for APIs
        last_name = request.POST.get('last_name')
        business_email = request.POST.get('business_email')
        company_name = request.POST.get('company_name')
        job_title = request.POST.get('job_title')
        phone_number = request.POST.get('phone_number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        obj = Prospect.objects.create(
                first_name=first_name,
                last_name=last_name,
                business_email=business_email,
                company_name=company_name,
                job_title=job_title,
                phone_number=phone_number,
                city=city,
                state=state,

        )
        return HttpResponseRedirect("/prospects")

    template_name = 'offices/prospect_form.html'
    context = {
    }
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
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Prospect.objects.filter(
                    Q(city__iexact=slug) |
                    Q(city__icontains=slug)
            )
        else:
            queryset = Prospect.objects.all()
        return queryset


class OfficeDetailView(DetailView):
    queryset = Prospect.objects.all()  # filter(country__iexact='USA')

    # def get_object(self, *args, **kwargs):
    #     off_id = self.kwargs.get('off_id')
    #     obj = get_object_or_404(Office, id=off_id) # pk = off_id
    #     return obj
