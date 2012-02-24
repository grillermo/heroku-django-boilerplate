from django import template

register = template.Library()

@register.filter(name='prefix') 
def prefix(value,prefix):
    return str(prefix)+str(value)
