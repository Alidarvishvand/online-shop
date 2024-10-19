from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class indexView(TemplateView):
    template_name = "./website/index.html"
    
class AboutView(TemplateView):
    template_name = "./website/about.html"
    
class ContactView(TemplateView):
    template_name = "./website/contact.html"