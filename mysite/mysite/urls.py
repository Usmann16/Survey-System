"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('TermOfUse.html', views.term),
    path('intro.html', views.intro, name='intro'),
    path('Question1.html', views.Question1, name='Question1'),
    path('Question2.html', views.Question2, name='Question2'),
    path('TextA.html', views.TextA, name='TextA'),
    path('TextB.html', views.TextB, name='TextB'),
    path('Thanks.html', views.Thanks, name='Thanks'),
    path('TextAEnhanced.html', views.TextAEnhanced, name='TextA Enhanced'),
    path('TextBEnhanced.html', views.TextBEnhanced, name='TextB Enhanced'),

]
