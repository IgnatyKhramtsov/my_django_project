from django import template
import myself.views as views


register = template.Library()

@register.simple_tag()    # можно указать имен. парам. например name='getcats'
def get_categories():
    return views.cats_db
