from django.db import models

from home.models import Formulaire


class FormulaireChargement(Formulaire):
    vehicule = models.CharField("Numéro de véhicule", max_length=255)
    bon_de_livraison = models.CharField("Numéro bon de livraison", max_length=255)
    sacs_sortis = models.IntegerField("Nombre de sacs à la fin du chargement")
    bonus = models.BooleanField("Chargement avec bonus ou pas", default=False)

    formulaire_ptr = models.OneToOneField(
        Formulaire, on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
        auto_created=True,
    )