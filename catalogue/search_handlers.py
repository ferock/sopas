from oscar.apps.catalogue.search_handlers import *
from oscar.core.loading import get_class, get_model

Product = get_model('catalogue', 'Product')



class SimpleProductSearchHandler(SimpleProductSearchHandler):
    def get_queryset(self):
        qs = Product.browsable.base_queryset().order_by("orden")
        if self.categories:
            qs = qs.filter(categories__in=self.categories).distinct()
        return qs
