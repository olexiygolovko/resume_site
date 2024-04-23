from django.shortcuts import render, redirect
from .models import *
from django_filters.views import FilterView
from .filters import PortfolioProjectFilter
from .forms import MessageForm


def home(request):
    slider = Slider.objects.all()
    about = Person.objects.first()
    services = Service.objects.all()
    education = Education.objects.all()
    portfolio = PortfolioProject.objects.all()
    languages = Language.objects.all()
    experience = Experience.objects.all()
    contacts = Contact.objects.all()
    categories = ProjectCategory.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        projects = PortfolioProject.objects.filter(category__name=selected_category)
    else:
        projects = PortfolioProject.objects.all()

    project_filter = PortfolioProjectFilter(request.GET, queryset=projects)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # или куда вы хотите перенаправить после отправки формы
    else:
        form = MessageForm()
        
    context = {
        'slider': slider,
        'about': about,
        'services': services,
        'education': education,
        'portfolio': portfolio,
        'languages': languages,
        'experience': experience,
        'categories': categories,
        'selected_category': selected_category,
        'filter': project_filter,
        'form': form,
        'contacts': contacts,
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

def main_page(request):
    person = Person.objects.first()

    context = {
        'person': person,
    }
    return render(request,'navigator.html', context)

def handler404(request, exception, template_name="404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response