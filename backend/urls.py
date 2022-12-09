from django.urls import path
from .views import HomeView,AboutView,AuthorView,ContactView,IndexFullLeft

urlpatterns = [
    path('',HomeView.as_view()),
    path('about/',AboutView.as_view()),
    path('author/',AuthorView.as_view()),
    path('contact/',ContactView.as_view()),
    path('indexfullleft/',IndexFullLeft.as_view())
]
