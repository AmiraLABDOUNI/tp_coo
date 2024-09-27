"""
URL configuration for crayon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from high_level import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "Ville/<int:pk>",
        views.VilleDetailView.as_view(),
        name="Ville",
    ),
    path(
        "Local/<int:pk>",
        views.LocalDetailView.as_view(),
        name="Local",
    ),
    path(
        "Usine/<int:pk>",
        views.UsineDetailView.as_view(),
        name="Usine",
    ),
    path(
        "Ressource/<int:pk>",
        views.RessourceDetailView.as_view(),
        name="Ressource",
    ),
    path(
        "QuantiteRessource/<int:pk>",
        views.QuantiteRessourceDetailView.as_view(),
        name="QuantiteRessource",
    ),
    path(
        "Produit/<int:pk>",
        views.ProduitDetailView.as_view(),
        name="Produit",
    ),
    path(
        "Machine/<int:pk>",
        views.MachineDetailView.as_view(),
        name="Machine",
    ),
    path(
        "Stock/<int:pk>",
        views.StockDetailView.as_view(),
        name="Stock",
    ),
    path(
        "Machine/<int:pk>",
        views.MachineDetailView.as_view(),
        name="Machine",
    ),
    path(
        "SiegeSocial/<int:pk>",
        views.SiegeSocialDetailView.as_view(),
        name="SiegeSocial",
    ),
    path(
        "Etape/<int:pk>",
        views.EtapeDetailView.as_view(),
        name="Etape",
    ),
]
