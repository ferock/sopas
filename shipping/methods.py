from  oscar.apps.shipping.abstract_models import *
from oscar.apps.shipping import methods
from oscar.core import prices


help(AbstractOrderAndItemCharges)
class FleteDefault(AbstractOrderAndItemCharges):
    code = 'flete1'
    name = 'Flete'

#   def calculate(self,basket):
#        return prices.Price(currency=basket.currency,
#            excl_tax=D('10.00'), incl_tax=D('10.00'))

class Free(methods.Free):
    code='free'
    name='Free'
