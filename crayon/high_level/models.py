from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField()
    prixm2 = models.IntegerField()


class Local(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(
        Ville,
        on_delete=models.CASCADE,
    )
    surface = models.IntegerField()

    class Meta:
        abstract = True


class Objet(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()

    class Meta:
        abstract = True


class Ressource(Objet):
    def __init__(self):
        pass


class Stock(models.Model):
    ressource = models.ForeignKey(
        Ressource,
        on_delete=models.CASCADE,
    )
    nombre = models.IntegerField()


class SiegeSocial(Local):
    def __init__(self):
        pass  # le constructeur fait rien psq la classe est vide y a pas de methode


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    n_serie = models.IntegerField()


class Usine(Local):
    machines = models.ForeignKey(
        Machine,
    )


class QuantiteRessource(models.Models):
    ressource = models.ForeignKey(
        Ressource,
        on_delete=models.CASCADE,
    )
    quantite = models.IntegerField()


class Etape(models.Models):
    nom = models.CharField(max_length=100)
    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
    )
    quantite_ressource = models.ForeignKey(
        QuantiteRessource,
        on_delete=models.CASCADE,
    )
    duree = models.IntegerField()
    etape_suivante = models.ForeignKey(
        "self",
        null=True,
        on_delete=models.CASCADE,
    )


class Produit(Objet):
    premier_etage = models.ForeignKey(
        Etape,
        on_delete=models.CASCADE,
    )
