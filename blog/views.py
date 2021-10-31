from django.shortcuts import render
from django.views.generic import TemplateView
import mimetypes
# Create your views here.
class Homepage(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class Services(TemplateView):
    template_name = 'services.html'

class Portfolio(TemplateView):
    template_name = 'portfolio.html'

class Bot(TemplateView):
    template_name = 'bot.html'

class Contact(TemplateView):
    template_name = 'contact.html'

