from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeView.as_view()),
    path('about/',AboutView.as_view(), name="about" ),
    path('author/',AuthorView.as_view(),name="author" ),
    path('contact/',ContactView.as_view() , name= "contact" ),
    path('indexfullleft/',IndexFullLeftView.as_view(),name="ifl" ),
    path('indexfullright/',IndexFullRightView.as_view() , name="ifr" ),
    path('indexfull/',IndexFullView.as_view() , name="if" ),
    path('indexlistleft/',IndexListLeftView.as_view() , name="ill" ),
    path('indexlistright/',IndexListRightView.as_view() , name="ilr"),
    path('indexlist/',IndexListView.as_view() , name="il"),
    path('postdetails1/',PostDetails1View.as_view(),name="pd1" ),
    path('postdetails2/',PostDetails2View.as_view() , name="pd2" ),
    path('postelements/',PostElementsView.as_view() , name="pe" ),
    path('privacypolicy/',PrivacyPolicyView.as_view() , name="pp"),
    path('termsconditions/',TermsConditionsView.as_view(), name="tc")
]
