from django.shortcuts import render
from .models import *
from django_filters.views import FilterView
from .filters import PortfolioProjectFilter


def home(request):
    slider = Slider.objects.all()
    about = Person.objects.first()
    services = Service.objects.all()
    portfolio = PortfolioProject.objects.all()
    languages = Language.objects.all()
    experience = Experience.objects.all()
    categories = ProjectCategory.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        projects = PortfolioProject.objects.filter(category__name=selected_category)
    else:
        projects = PortfolioProject.objects.all()

    project_filter = PortfolioProjectFilter(request.GET, queryset=projects)

    context = {
        'slider': slider,
        'about': about,
        'services': services,
        'portfolio': portfolio,
        'languages': languages,
        'experience': experience,
        'categories': categories,
        'selected_category': selected_category,
        'filter': project_filter,
    }

    return render(request, 'home.html', context)


def about(request):
    about = Person.objects.first()
    languages = Language.objects.all()

    context = {
        'about': about,
        'languages': languages,
    }

    return render(request, 'about.html', context)

def language(request):
    languages = Language.objects.all()
    context = {
        'languages': languages,
    }
    return render(request, 'languages_block.html', context)

def education(request):
    title = Education.objects.all()
    speciality = Education.objects.all()
    context = {
        'title': title,
        'speciality': speciality,
    }

    return render(request,'education.html', context)


def main_page(request):
    person = Person.objects.first()

    context = {
        'person': person,
    }
    return render(request,'navigator.html', context)
