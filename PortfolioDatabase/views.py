from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby, Portfolio


# Create your views here.
def home(request):
    context = {}
    return render(request, "PortfolioDatabase/home.html", context)


def hobbies(request):
    hobby_list = Hobby.objects.all()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, "PortfolioDatabase/hobbies.html", context)


def hobby_detail(request, item_id):
    item = Hobby.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, "PortfolioDatabase/detail.html", context)


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolio_list': portfolio_list,
    }
    return render(request, "PortfolioDatabase/portfolio.html", context)


def portfolio_detail(request, item_id):
    item = Portfolio.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, "PortfolioDatabase/detail.html", context)


def contact(request):
    context= {}
    return render(request, "PortfolioDatabase/contact.html", context)


