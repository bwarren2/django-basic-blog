from django import template
from markdown import markdown

register = template.Library()


@register.filter('markdownify')
def markdownify(text):
    return markdown(text)
