from django.shortcuts import render
from .models import Carousel, About, Box, Action, Service, Portfolio, Testimonial, Pricing, Faq, Team, Blog, Contact


# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def home(request):
    context = {
        'carousels': Carousel.objects.all(),
        'about': About.objects.all(),
        'box': Box.objects.all(),
        'action': Action.objects.all(),
        'service': Service.objects.all(),
        'portfolio': Portfolio.objects.all(),
        'testimonial': Testimonial.objects.all(),
        'pricing': Pricing.objects.all(),
        'faq': Faq.objects.all(),
        'team': Team.objects.all(),
        'blog': Blog.objects.all(),
        'contact': Contact.objects.all(),
    }
    return render(request, 'home.html', context={})


# def form(request):
#     return render(request, )