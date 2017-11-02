from oscar.apps.shipping import repository
from . import methods
from  oscar.apps.shipping.abstract_models import *

class Repository(repository.Repository):


    methods = ()

    def get_default_shipping_method(self, basket, shipping_addr=None, **kwargs):
        help(methods.FleteDefault())
        return self.get_shipping_methods(basket, shipping_addr=None, **kwargs)[0]

    def get_shipping_methods (self, basket, shipping_addr=None, **kwargs):
        self.get_available_shipping_methods(basket=basket, shipping_addr=shipping_addr, **kwargs)
        return self.methods

    def get_available_shipping_methods(self, basket, shipping_addr=None,**kwargs):
        self.methods = (methods.FleteDefault(),)
