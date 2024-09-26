from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField()
    prixm2 = models.IntegerField()

    def __str__(self):
        return self.nom


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
    def __str__(self):
        return self.nom


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    n_serie = models.IntegerField()

    def __str__(self):
        return self.nom

    def costs(self):
        return self.prix


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


class SiegeSocial(Local):
    def __str__(self):
        return self.nom


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


class Produit(Objet):
    premiere_etape = models.ForeignKey(
        Etape,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.nom
