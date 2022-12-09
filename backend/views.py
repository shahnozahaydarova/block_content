from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class AuthorView(TemplateView):
    template_name = 'author.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
class IndexFullLeft(TemplateView):
    template_name = 'index-full-left.html'
