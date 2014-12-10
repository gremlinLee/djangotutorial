from django.template import Library

register = Library()


@register.filter
def is_true(value, arg):
    print 'hello from filter', value, arg
    return value is True