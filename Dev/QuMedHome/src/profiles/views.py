import random
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# # function base view

def home(request):
    num = None
    some_list = [random.randint(0, 100000), random.randint(0, 100000), random.randint(0, 100000)]
    condition_bool_item = True
    if condition_bool_item:
        num = random.randint(0, 100000)
    context = {'html_var': True,
               'num': num,
               'some_list': some_list}
    return render(request, 'home.html', context)

def contact(request):

    context = {}
    return render(request, 'contact.html', context)

def referrals(request):

    context = {}
    return render(request, 'referrals.html', context)

def appointments(request):

    context = {}
    return render(request, 'appointments.html', context)
