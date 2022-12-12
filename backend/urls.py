from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeView.as_view()),
    path('about/',AboutView.as_view()),
    path('author/',AuthorView.as_view()),
    path('contact/',ContactView.as_view()),
    path('indexfullleft/',IndexFullLeftView.as_view()),
    path('indexfullright/',IndexFullRightView.as_view()),
    path('indexfull/',IndexFullView.as_view()),
    path('indexlistleft/',IndexListLeftView.as_view()),
    path('indexlistright/',IndexListRightView.as_view()),
    path('indexlist/',IndexListView.as_view()),
    path('postdetails1/',PostDetails1View.as_view()),
    path('postdetails2/',PostDetails2View.as_view()),
    path('postelements/',PostElementsView.as_view()),
    path('privacypolicy/',PrivacyPolicyView.as_view()),
    path('termsconditions/',TermsConditionsView.as_view())
]
