from django.shortcuts import render
from ecommerce.models import Category


def index(request):
    category = Category.objects.all()
    context = {
        'categories': category,
    }
    return render(request, 'ecommerce/index.html', context)
