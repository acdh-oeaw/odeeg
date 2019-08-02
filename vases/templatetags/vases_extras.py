from django import template

register = template.Library()


@register.simple_tag
def get_item_by_type(obj, item_type):
    return obj.get_item_by_type(item_type)


@register.simple_tag
def get_item_by_mime(obj, item_mime):
    return obj.get_item_by_mime(item_mime)
