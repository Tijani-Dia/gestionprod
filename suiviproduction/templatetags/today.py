from django import template

from datetime import date

register = template.Library()

@register.inclusion_tag('include/today.html')
def today():
    
    return {'today': date.today().strftime("%d-%m-%Y")}
