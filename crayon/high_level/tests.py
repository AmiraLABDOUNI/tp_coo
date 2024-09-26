# Create your tests here.
from django.test import TestCase
from .models import Machine
from .models import Usine
from .models import Ressource
from .models import Stock
from .models import Ville

# class MachineModelTests(TestCase):
# def test_machine1_creation(self):
#    self.assertEqual(Machine.objects.count(), 0)
#    Machine.objects.create(nom="scie", prix=1_000, n_serie=25)
#    self.assertEqual(Machine.objects.count(), 1)


class UsineModelTests(TestCase):
    def test_usine_costs(self):
        v = Ville.objects.create(nom="Labege", prixm2=2_000, code_postal="45000")
        m1 = Machine.objects.create(nom="scie", prix=1_000, n_serie=25)
        m2 = Machine.objects.create(nom="yoho", prix=2_000, n_serie=12)
        u = Usine.objects.create(ville=v, nom="usine1", surface=50)
        u.machines.add(m1)
        u.machines.add(m2)
        r1 = Ressource.objects.create(ressource="bois", prix="10")
        r2 = Ressource.objects.create(ressource="mine", prix="15")
        Stock.objects.create(ressource=r1, nombre="1_000", usine=u)
        Stock.objects.create(ressource=r2, nombre="50", usine=u)
        self.assertEqual(u.costs(), 110_750)
