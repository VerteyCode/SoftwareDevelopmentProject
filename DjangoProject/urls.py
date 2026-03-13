"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from nautilus_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='MainPage.html'), name='MainPage'),
    path('consultation/', views.ConsultationPage, name='ConsultationPage'),
    path('review/', views.ReviewPage, name='ReviewPage'),
    path('team/', views.TeamPage, name='TeamPage'),
    path('pricing/', views.PricingPage, name='PricingPage'),
    path('landing/', views.LandingPage, name='LandingPage'),

]
