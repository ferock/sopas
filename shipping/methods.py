from  oscar.apps.shipping.abstract_models import *
from oscar.apps.shipping import methods
from oscar.core import prices

class Free(methods.Free):
    code = 'self-pickup'
    name = ('Self pickup')


class FleteDefault(methods.FixedPrice):
    code = 'flete'
    name = ('Flete')

    charge_excl_tax = D("35.00")
    charge_incl_tax = D("35.00")
