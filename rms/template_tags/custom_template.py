from calendar import month_name
from django import template
import locale

locale.setlocale(locale.LC_ALL, '')
register = template.Library()


@register.filter()
def get_month_name(month):
    return month_name[month]
