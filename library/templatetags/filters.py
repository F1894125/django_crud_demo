from django import template

register = template.Library()

@register.filter
def replace(value, arg):
    if ',' not in arg:
        return value
        
    old, new = arg.split(',', 1)
    return str(value).replace(old, new)