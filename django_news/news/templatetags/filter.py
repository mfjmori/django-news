from django import template
import datetime
import dateutil.parser

register = template.Library()
@register.filter(expects_localtime=True)
def parse_date(value):
  return dateutil.parser.parse(value)
