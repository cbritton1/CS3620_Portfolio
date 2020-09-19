from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby, Portfolio


# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome</h1>'
                        '<p>My name is Cory and I am trying to learn Django :)')


def hobbies(request):
    hobby_list = Hobby.objects.all()
    return HttpResponse(hobby_list)


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    return HttpResponse(portfolio_list)


def contact(request):
    return HttpResponse('contact')
