from django.contrib import admin
from django.urls import path
from backend.views import HomeView,AboutView,ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view()),
    path('about/',AboutView.as_view()),
    path('contact/',ContactView.as_view())
]
