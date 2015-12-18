from django import template
from markdown import markdown

register = template.Library()


@register.filter
def markdownify(text):
    return markdown(text)
