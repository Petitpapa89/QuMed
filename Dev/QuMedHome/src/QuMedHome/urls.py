"""QuMedHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

from offices.views import (office_list_view,
                           OfficeListView,
                           OfficeDetailView,
                           prospect_create_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^referrals/$', TemplateView.as_view(template_name="referrals.html")),
    url(r'^prospects/$', OfficeListView.as_view()),
    # url(r'^offices/(?P<slug>\w+)/$', OfficeListView.as_view()),
    url(r'^offices/(?P<slug>[\w-]+)/$', OfficeDetailView.as_view()),

    url(r'^appointments/$', TemplateView.as_view(template_name="appointments.html")),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html")),

    url(r'^create/$', prospect_create_view),
]
