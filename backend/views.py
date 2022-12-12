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

class IndexFullLeftView(TemplateView):
    template_name = 'index-full-left.html'

class IndexFullRightView(TemplateView):
    template_name = 'index-full-right.html'

class IndexFullView(TemplateView):
    template_name = 'index-full.html'

class IndexListLeftView(TemplateView):
    template_name = 'index-list-left.html'

class IndexListRightView(TemplateView):
    template_name = 'index-list-right.html'

class IndexListView(TemplateView):
    template_name = 'index-list.html'

class PostDetails1View(TemplateView):
    template_name = 'post-details-1.html'

class PostDetails2View(TemplateView):
    template_name = 'post-details-2.html'

class PostElementsView(TemplateView):
    template_name = 'post-elements.html'

class PrivacyPolicyView(TemplateView):
    template_name = 'privacy-policy.html'

class TermsConditionsView(TemplateView):
    template_name = 'terms-conditions.html'
