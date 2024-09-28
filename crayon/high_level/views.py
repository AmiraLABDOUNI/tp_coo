from django.views.generic import DetailView
from django.http import JsonResponse # Importer JsonResponse pour renvoyer des réponses au format JSON
from .models import Machine
from .models import Usine
from .models import Ressource
from .models import Stock
from .models import Ville
from .models import Etape
from .models import QuantiteRessource
from .models import SiegeSocial
from .models import Produit
from .models import Local
from .models import Objet
# Create your views here.

# Chaque view ns permet d'afficher le détail d'un modèle en réponse au format JSON

class VilleDetailView(DetailView):
    model = Ville

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class StockDetailView(DetailView):
    model = Stock
   # Méthode pour renvoyer la réponse au format JSON
    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class RessourceDetailView(DetailView):
    model = Ressource

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class UsineDetailView(DetailView):
    model = Usine

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class MachineDetailView(DetailView):
    model = Machine

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class LocalDetailView(DetailView):
    model = Local

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class ObjetDetailView(DetailView):
    model = Objet

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class QuantiteRessourceDetailView(DetailView):
    model = QuantiteRessource

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class SiegeSocialDetailView(DetailView):
    model = SiegeSocial

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class ProduitDetailView(DetailView):
    model = Produit

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class EtapeDetailView(DetailView):
    model = Etape

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())
