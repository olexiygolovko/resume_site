import django_filters
from .models import PortfolioProject


class PortfolioProjectFilter(django_filters.FilterSet):
    class Meta:
        model = PortfolioProject
        fields = {
            'category__name': ['exact'],
        }
