from django.urls import path
from .views import Homepage, Contact, Services, Bot, About, Portfolio

urlpatterns = [
    path('', Homepage.as_view(), name='Home'),
    path('about/', About.as_view(), name='About'),
    path('services/', Services.as_view(), name='Services'),
    path('portfolio/', Portfolio.as_view(), name='Portfolio'),
    path('portfolio/bot/', Bot.as_view(), name='Bot'),
    path('contact/', Contact.as_view(), name='Contact'),
]