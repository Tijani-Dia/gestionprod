from django import template

from suiviqualite.models import MachineEnsacheuse

register = template.Library()

LABELS_PC = [
    {
        'name': 'chlore_libre',
        'label': 'Chlore Libre',
        'id': 'chlore_libre',
        'unite': 'mg/L',
        'required': True
    },
    {
        'name': 'chlore_total',
        'label': 'Chlore Total',
        'id': 'chlore_total',
        'unite': 'mg/L',
        'required': True
    },
    {
        'name': 'turbidite',
        'label': 'Turbidite',
        'id': 'turbidite',
        'unite': 'NTU',
        'required': True
    },
    {
        'name': 'ph',
        'label': 'PH',
        'id': 'ph',
        'unite': '',
        'required': True
    },
    {
        'name': 'durete',
        'label': 'Dureté',
        'id': 'durete',
        'unite': '',
        'required': True
    },
    {
        'name': 'nitrate',
        'label': 'Nitrate',
        'id': 'nitrate',
        'unite': 'mg/L',
        'required': False
    }
]

LABELS_MICRO = [
    {
        'name': 'microorganismes_22',
        'label': 'Microorganismes revivifiables 22°C',
        'id': 'micro_22',
        'required': True
    },
    {
        'name': 'microorganismes_36',
        'label': 'Microorganismes revivifiables 36°C',
        'id': 'micro_36',
        'required': True
    },
    {
        'name': 'microorganismes_44',
        'label': 'Microorganismes revivifiables 44°C',
        'id': 'micro_44',
        'required': True
    },
    {
        'name': 'coliformes_totaux',
        'label': 'Coliformes totaux',
        'id': 'coliformes_totaux',
        'required': True
    },
    {
        'name': 'coliformes_fecaux',
        'label': 'Coliformes fécaux',
        'id': 'coliformes_fecaux',
        'required': True
    },
    {
        'name': 'e_coli',
        'label': 'E-COLI',
        'id': 'e_coli',
        'required': False
    }
]

@register.inclusion_tag('include/pc-form.html')
def pc_form():
    return {'labels': LABELS_PC}

@register.inclusion_tag('include/metro-form.html')
def metro_form():
    return {
        'machines': MachineEnsacheuse.objects.all()
    }

@register.inclusion_tag('include/micro-form.html')
def micro_form():
    return {'labels': LABELS_MICRO}


@register.inclusion_tag('include/pc-modify-form.html')
def pc_modify_form(element):
    labels = LABELS_PC
    for label in labels:
        label["value"] = getattr(element, label['name'])

    return {
        'labels': labels,
        'element_id': element.id,
        'obs': element.observation
    }


@register.inclusion_tag('include/micro-modify-form.html')
def micro_modify_form(element):
    labels = LABELS_MICRO
    for label in labels:
        label["value"] = getattr(element, label['name'])

    return {
        'labels': labels,
        'element_id': element.id,
        'obs': element.observation,
        'pseudomonas': element.pseudomonas
    }


@register.inclusion_tag('include/metro-modify-form.html')
def metro_modify_form(element):
    return {
        'element_id': element.id,
        'obs': element.observation,
        'poids': element.poids,
        'el_machine': element.machine,
        'quart': element.quart,
        'machines': MachineEnsacheuse.objects.all()
    }