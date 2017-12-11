from django.db.models import *

from oscar.apps.catalogue.abstract_models import AbstractProduct

class Product(AbstractProduct):
    orden = IntegerField(default=-1)

from oscar.apps.catalogue.models import *
