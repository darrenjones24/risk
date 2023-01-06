"""risk_neutral_player URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from website.views import (
    players,
    show_positions,
    reinforce,
    comp_lose_country,
    comp_gain_country,
    current_positions,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", players),
    path("players", players),
    path("show_positions", show_positions),
    path("reinforce", reinforce),
    path("comp_lose_country", comp_lose_country),
    path("comp_gain_country", comp_gain_country),
    path("current_positions", current_positions),
]
