from django import template
import myself.views as views
from myself.models import Category

register = template.Library()

'''@register.simple_tag()    # можно указать имен. парам. например name='getcats'
def get_categories():
    return views.cats_db'''

@register.inclusion_tag('myself/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
