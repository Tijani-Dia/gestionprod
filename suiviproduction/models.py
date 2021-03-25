from django.db import models
from django.conf import settings

import datetime

from home.models import Formulaire


class FormulaireProduction(Formulaire):
    QUART_CHOICES = [
        ('Q1', '1er Quart'),
        ('Q2', '2e Quart'),
        ('Q3', '3e Quart'),
    ]
    quart_de_production = models.CharField("Quart de Production", choices=QUART_CHOICES, max_length=2)
    sacs_produits = models.IntegerField("Nombre de sacs produits")

    formulaire_ptr = models.OneToOneField(
        Formulaire, on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
        auto_created=True,
    )


class FormulaireCasse(Formulaire):
    casses_recues = models.IntegerField("Casses reçues", default=0)
    casses_traitees = models.IntegerField("Casses traitées", default=0)
    dotation_commerciaux = models.IntegerField("Dotation commerciaux", default=0)
    dotation_personnel = models.IntegerField("Dotation au personnel (Frigo interne)", default=0)
    retour_commerciaux =  models.IntegerField("Retour commerciaux", default=0)
    casse_reelle = models.IntegerField("Casse réelle", default=0)

    formulaire_ptr = models.OneToOneField(
        Formulaire, on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
        auto_created=True,
    )

    @property
    def casses_perdues(self):
        return self.dotation_commerciaux + self.dotation_personnel + self.retour_commerciaux + self.casse_reelle


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
    return FormulaireProduction.objects.filter(date__date=date).filter(quart_de_production='Q{}'.format(quart))
    


