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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from offices.views import (office_list_view,
                           OfficeListView,
                           OfficeDetailView,
                           prospect_create_view,
                           ProspectCreateView
                           )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name="aboutQumed.html"), name='about'),

    url(r'^prospects/$', OfficeListView.as_view(), name='prospects'),
    # url(r'^prospects/$', ProspectCreateView.as_view()),
    url(r'^offices/(?P<slug>[\w-]+)/$', OfficeDetailView.as_view()),

    url(r'^products/$', TemplateView.as_view(template_name="products.html"), name='products'),
    # url(r'^contact/$', TemplateView.as_view(template_name="contact.html")),

    url(r'^create/$', prospect_create_view, name='create'),#ProspectCreateView.as_view()),
    # url(r'^create/$', ProspectCreateView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()