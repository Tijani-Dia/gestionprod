from django import template
import datetime
from suiviproduction.models import FormulaireCasse

register = template.Library()

LABELS_CASSE = [
    {
        'name': 'casses_recues',
        'label': 'Casses Reçues',
        'id': 'casses_recues'
    },
    {
        'name': 'casses_traitees',
        'label': 'Casses Traitées',
        'id': 'casses_traitees'
    },
    {
        'name': 'dotation_commerciaux',
        'label': 'Dotation Commerciaux',
        'id': 'dotation_commerciaux'
    },
    {
        'name': 'dotation_personnel',
        'label': 'Dotation Personnel (Frigo)',
        'id': 'dotation_personnel'
    },
    {
        'name': 'retour_commerciaux',
        'label': 'Retour Commerciaux',
        'id': 'retour_commerciaux'
    },
    {
        'name': 'casse_reelle',
        'label': 'Casse Réelle',
        'id': 'casse_reelle'
    }
]


@register.inclusion_tag('include/prod-modify-form.html')
def prod_modify_form(element):

    return {
        'sacs': element.sacs_produits,
        'element_id': element.id,
        'obs': element.observation,
        'quart': element.quart_de_production
    }


@register.inclusion_tag('include/casse-form.html')
def casse_form():

    labels = LABELS_CASSE
    filled = FormulaireCasse.objects.filter(
        date__date=datetime.date.today()
    )

    if filled:
        # Make sure only one form has been filled
        assert len(filled) == 1
        filled_today = filled[0]
        for label in labels:
            label["value"] = getattr(filled_today, label['name'])

        return {
            'labels': labels,
            'element_id': filled_today.id,
            'obs': filled_today.observation
        }

    return {
        'labels': labels
    }
