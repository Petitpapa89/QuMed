import random
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# # function base view

def home(request):
    num = random.randint(0, 100000)
    some_list = [num, random.randint(0, 100000), random.randint(0, 100000)]
    context = {"html_var": True,
               'num': num,
               'bool_item': False,
               'some_list': some_list}
    return render(request, 'base.html', context)
