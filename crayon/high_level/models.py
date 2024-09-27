from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField()
    prixm2 = models.IntegerField()

    def __str__(self):
        return self.nom

    # conversion de la data au format json
    def json(self):
        d = {
            "nom": self.nom,
            "code_postal": self.code_postal,
            "prixm2": self.prixm2,
        }
        return d


class Local(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(
        Ville,
        on_delete=models.CASCADE,
    )
    surface = models.IntegerField()

    # conversion de la data au format json
    def json(self):
        d1 = {
            "nom": self.nom,
            "ville": self.ville.id,  # il va se référer au id de la ville car on a un ForeignKey
            "surface": self.surface,
        }
        return d1

    class Meta:  # classe mere
        abstract = True


class Objet(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()

    # conversion de la data au format json
    def json(self):
        d2 = {
            "nom": self.nom,
            "prix": self.prix,
        }
        return d2

    class Meta:  # classe mere
        abstract = True


class Ressource(Objet):
    def __str__(self):
        return self.nom


# ressource herite d'objet et le json existe deja en objet donc pas la peine de le refaire pr ressource


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    n_serie = models.IntegerField()

    def __str__(self):
        return self.nom

    def costs(self):
        return self.prix

    def json(self):
        d3 = {
            "nom": self.nom,
            "prix": self.prix,
            "n_serie": self.n_serie,
        }
        return d3


class Usine(Local):
    machines = models.ManyToManyField(
        Machine,
    )

    def __str__(self):
        return self.nom

    def costs(self):
        cost = 0
        costmachine = 0
        ress = 0
        for machines in self.machines.all():
            costmachine = machines.costs()

        for stock in self.stock_set.all():
            ress = stock.ressource.prix * stock.nombre

        cost = (ress + costmachine) + (self.surface * self.ville.prixm2)

        return cost

    def json(self):
        machines_list = []  # Initialisation d'une liste vide pour les machines
        for machine in self.machines.all():
            machines_list.append(
                {"nom": machine.nom, "prix": machine.prix, "n_serie": machine.n_serie}
            )  # Ajout des informations de chaque machine à la liste
        d4 = {
            "nom": self.nom,
            "ville": self.ville.id,
            "surface": self.surface,
            "machines": machines_list,  # Liste des machines
        }

        return d4  # Conversion du dictionnaire en JSON


class Stock(models.Model):
    ressource = models.ForeignKey(
        Ressource,
        on_delete=models.CASCADE,
    )
    nombre = models.IntegerField()
    usine = models.ForeignKey(
        Usine,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.ressource}: {self.nombre }"

    def json(self):
        d5 = {
            "Ressource": self.ressource.id,
            "nombre": self.nombre,
            "usine": self.usine.id,
        }
        return d5


class SiegeSocial(Local):
    def __str__(self):
        return self.nom


# siege SiegeSocial herite du local  et le json existe deja en local donc pas la peine de le refaire


class QuantiteRessource(models.Model):
    ressource = models.ForeignKey(
        Ressource,
        on_delete=models.CASCADE,
    )
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.ressource}: {self.quantite}"

    def costs(self):
        return {self.quantite * self.ressource.prix}

    def json(self):
        d6 = {
            "ressource": self.ressource.id,
            "quantite": self.quantite,
        }
        return d6


class Etape(models.Model):
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
        blank=True,
    )

    def __str__(self):
        return self.nom

    def json(self):
        d7 = {
            "nom": self.nom,
            "machine": self.machine.id,
            "quantite_ressource": self.quantite_ressource.id,
            "duree": self.duree,
        }
        if self.etape_suivante:
            d7["etape_suivante"] = (self.etape_suivante.id,)

        return d7


class Produit(Objet):
    premiere_etape = models.ForeignKey(
        Etape,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.nom

    def json(self):
        d8 = {
            "nom": self.nom,
            "prix": self.prix,
            # "premiere_etape": self.premiere_etape.id,
        }
        # if self.premiere_etape:
        #    d8["premiere_etape"] = self.premiere_etape.id

        return d8
