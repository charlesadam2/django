from django.shortcuts import render
from .models import Carousel, About, Box, Action, Service, Portfolio, Testimonial, Pricing, Faq, Team, Blog, Contact


# Create your views here.

def blog(request):
    return render(request, 'blog.html')

def home(request):
    carousels = Carousel.objects.all()
    abouts = About.objects.all()
    boxs = Box.objects.all()
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = Faq.objects.all()
    teams = Team.objects.all()
    blogs = Blog.objects.all()
    contacts = Contact.objects.all()

    context = {
        'carousels':  Carousel.objects.all(),
        'abouts': About.objects.all(),
        'boxs': Box.objects.all(),
        'actions': Action.objects.all(),
        'services': Service.objects.all(),
        'portfolios': Portfolio.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'pricings': Pricing.objects.all(),
        'faqs': Faq.objects.all(),
        'teams': Team.objects.all(),
        'blogs': Blog.objects.all(),
        'contacts': Contact.objects.all(),
    }
    return render(request, 'home.html', context)


# def form(request):
#     return render(request, )