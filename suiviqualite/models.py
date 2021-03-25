from django.db import models

import datetime

from home.models import Formulaire

class MachineEnsacheuse(models.Model):
    """
    A model for a Machine Ensacheuse for weight.
    """
    machine_code = models.CharField("Code Machine Ensacheuse", max_length=4)

    def __str__(self):
        return self.machine_code



class ParametresPhysicoChimiques(Formulaire):
    chlore_libre = models.FloatField("Chlore Libre")
    chlore_total = models.FloatField("Chlore Total")
    turbidite = models.FloatField("Turbidité")
    ph = models.FloatField("PH")
    durete = models.IntegerField("Dureté")
    nitrate = models.FloatField("Nitrate", null=True, blank=True)
    formulaire_ptr = models.OneToOneField(
        Formulaire, on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
        auto_created=True,
    )

    def is_problematic_chlore_libre(self):
        return self.chlore_libre > 1

    def is_problematic_chlore_total(self):
        return self.chlore_total > 2

    def is_problematic_turbidite(self):
        return self.turbidite > 1

    def is_problematic_ph(self):
        return self.ph < 6.5 or self.ph > 8

    def is_problematic_durete(self):
        return self.durete > 20

    def is_problematic_nitrate(self):
        return self.nitrate > 0


class ParametresMicrobiologiques(Formulaire):
    microorganismes_22 = models.IntegerField("MICROORGANISMES REVIVIFIABLES 22°C", default=0)
    microorganismes_36 = models.IntegerField("MICROORGANISMES REVIVIFIABLES 36°C", default=0)
    microorganismes_44 = models.IntegerField("MICROORGANISMES REVIVIFIABLES 44°C", default=0)
    coliformes_totaux = models.IntegerField("COLIFORMES TOTAUX", default=0)
    coliformes_fecaux = models.IntegerField("COLIFORMES FECAUX", default=0)
    e_coli = models.IntegerField("E.COLI", default=0, null=True, blank=True)
    A_P_CHOICES = [
        ('A', 'Absence'),
        ('P', 'Présence'),
    ]
    pseudomonas = models.CharField("pseudomonas", default="A", choices=A_P_CHOICES, max_length=1)

    formulaire_ptr = models.OneToOneField(
        Formulaire, on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
        auto_created=True,
    )


    def is_problematic_micro_22(self):
        return self.microorganismes_22 >= 100

    def is_problematic_micro_36(self):
        return self.microorganismes_36 >= 100

    def is_problematic_micro_44(self):
        return self.microorganismes_44 >= 100

    def is_problematic_coliformes_totaux(self):
        return self.coliformes_totaux > 0

    def is_problematic_coliformes_fecaux(self):
        return self.coliformes_fecaux > 0

    def is_problematic_e_coli(self):
        return self.e_coli > 0

    def is_problematic_pseudomonas(self):
        return self.pseudomonas == "P"


class ParametresMetrologiques(Formulaire):
    poids = models.IntegerField()
    machine = models.ForeignKey(MachineEnsacheuse, on_delete=models.CASCADE)
    QUART_CHOICES = [
        ('Q1', '1er Quart'),
        ('Q2', '2e Quart'),
        ('Q3', '3e Quart'),
    ]
    quart = models.CharField("Quart de Production", choices=QUART_CHOICES, max_length=2)
    formulaire_ptr = models.OneToOneField(
        Formulaire, on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
        auto_created=True,
    )



    def is_problematic_poids(self):
        return self.poids <= 390 or self.poids >= 410 



def get_latest_by_date_and_quart():
    """Returns a dict of dicts where each is dict
    represents a day and the values inside represent the
    parameters by quart."""
    base = datetime.date.today()
    result = {}
    date_list = [base - datetime.timedelta(days=x) for x in range(7)]
    for date in date_list:
        result['{}'.format(date)] = {
            'quart_un': get_quart(1, date),
            'quart_deux': get_quart(2, date),
            'quart_trois': get_quart(3, date)
        }

    return result

def get_quart(quart, date):
    """ Returns completed forms in the
    given quart for the given date """
    return ParametresMetrologiques.objects.filter(date__date=date).filter(quart='Q{}'.format(quart))

