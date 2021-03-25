from django import template

register = template.Library()



@register.inclusion_tag('include/charg-modify-form.html')
def charg_modify_form(element):
    return {
        'element_id': element.id,
        'obs': element.observation,
        'vehicule': element.vehicule,
        'bon_de_livraison': element.bon_de_livraison,
        'sacs': element.sacs_sortis,
        'bonus': element.bonus
    }