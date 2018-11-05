import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, DetailView, CreateView, ListView
from django.core.mail import mail_admins, BadHeaderError, send_mail, EmailMessage

# from django.views.generic.list import ListView

from .forms import ProspectCreateForm, ProspectModelCreateForm
from .models import Prospect


# @login_required()  # we wont need to this site, but nice to know how
def prospect_create_view(request):
    form = ProspectModelCreateForm(request.POST or None)
    errors = None

    if form.is_valid():
        instance = form.save(commit=False)
        # instance.owner = request.user
        instance.save()
        send_email(request)

        return HttpResponseRedirect("/confirmation/")
        # return HttpResponseRedirect("/prospects/")

        # if request.user.is_authenticated():  # idk if we'll need this for the corp site
        #     instance = form.save(commit=False)
        #     instance.owner = request.user
        #     instance.save()
        #     return HttpResponseRedirect("/prospects/")
        # else:
        #     return HttpResponseRedirect("/login/")
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


class ProspectCreateView(CreateView):
    form_class = ProspectModelCreateForm
    template_name = 'offices/prospect_form.html'
    success_url = "/prospects/"


def send_email(request):
    subject = request.POST.get('company_name', '')
    message = request.POST.get('message', 'New Business Inquiry')
    from_email = request.POST.get('business_email', '')
    to_email = ['ydjiba89@gmail.com']

    if subject and message and from_email:
        try:
            email = EmailMessage(subject=subject, body=message, to=to_email)
            email.send()

            msg_sent = "have email has been sent"
            print ('msg sent', msg_sent)
            messages.success(request, msg_sent)
        except BadHeaderError:
            return HttpResponse('Invalid Header found.')
        # return HttpResponseRedirect('/confirmation/')
    else:
        return HttpResponse('Make sure all fields are entered and valid')
