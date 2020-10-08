from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hobby, Portfolio
from .forms import ContactForm, PortfolioForm


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
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:home')

    context = {
        'form': form
    }
    return render(request, "PortfolioDatabase/contact.html", context)


def edit_item(request, id):
    item = Portfolio.objects.get(id=id)
    form = PortfolioForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:portfolio')

    return render(request, 'PortfolioDatabase/portfolio-form.html', {'form': form, 'item': item})


def create_portfolio_item(request):
    form = PortfolioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:portfolio')
    return render(request, 'PortfolioDatabase/portfolio-form.html', {'form': form})


def delete_portfolio_item(request, id):
    item = Portfolio.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('PortfolioDatabase:portfolio')

    return render(request, 'PortfolioDatabase/portfolio-delete-item.html', {'item': item})
