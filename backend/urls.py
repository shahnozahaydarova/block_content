from django.urls import path
from .views import HomeView,AboutView,AuthorView,ContactView,IndexFullLeftView,IndexFullRightView,IndexFullView,IndexListLeftView
urlpatterns = [
    path('',HomeView.as_view()),
    path('about/',AboutView.as_view()),
    path('author/',AuthorView.as_view()),
    path('contact/',ContactView.as_view()),
    path('indexfullleft/',IndexFullLeftView.as_view()),
    path('indexfullright/',IndexFullRightView.as_view()),
    path('indexfull/',IndexFullView.as_view()),
    path('indexlistleft/',IndexListLeftView.as_view())
]
