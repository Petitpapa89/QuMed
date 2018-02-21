import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.

# class based views
class HomeView(TemplateView):
    """"""
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = None
        some_list = [random.randint(0, 100000), random.randint(0, 100000), random.randint(0, 100000)]
        condition_bool_item = True
        if condition_bool_item:
            num = random.randint(0, 100000)
        context = {'html_var': True,
                   'num': num,
                   'some_list': some_list}
        return context

