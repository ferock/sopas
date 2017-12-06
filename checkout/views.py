from oscar.apps.checkout import views
from oscar.apps.payment import models
from oscar.apps.payment.forms import BankcardForm
from oscar.apps.payment.exceptions import RedirectRequired
from paybac import  facade


class PaymentDetailsView(views.PaymentDetailsView):

    def get_context_data(self, **kwargs):
        ctx = super(PaymentDetailsView, self).get_context_data(**kwargs)
        ctx["tipo"] = ""
        ctx["efectivo"] = ""
        ctx["tipo"] = ""
        ctx["ccName"] = ""
        ctx["ccNumber"] = ""
        ctx["ccMonth"] = ""
        ctx["ccYear"] = ""
        ctx["ccCCV"] = ""
        if(kwargs.get('tipo', "")):
            if (kwargs.get('tipo', "")[0] == "efectivo"):
                ctx["tipo"] = kwargs.get("tipo", "")[0]
                ctx["efectivo"] = kwargs.get('efectivo', "")[0]
            else:
                if kwargs.get('tipo', "") == "tarjeta":
                    ctx["tipo"] = kwargs.get('tipo', "")[0]
                    ctx["ccName"] = kwargs.get('ccName', "")[0]
                    ctx["ccNumber"] = kwargs.get('ccNumber', "")[0]
                    ctx["ccMonth"] = kwargs.get('ccMonth', "")[0]
                    ctx["ccYear"] = kwargs.get('ccYear', "")[0]
                    ctx["ccCCV"] = kwargs.get('ccCCV', "")[0]
        return ctx

    def handle_place_order_submission(self,request):
        sub = self.build_submission()
        sub["payment_kwargs"] = request.POST
        return self.submit(**sub)

    def handle_payment_details_submission(self, request):
        return self.render_preview(request,**request.POST)

    def handle_payment(self, order_number, total, **kwargs):
        payment = kwargs
        if(payment.get("tipo")[0] == "efectivo"):
            reference="pagoEfectivo"
            print(float(payment.get("efectivo")[0]))
            source_type, __ = models.SourceType.objects.get_or_create(
                name="PagoEfectivo")
            source = models.Source(
                source_type=source_type,
                amount_allocated=total.incl_tax,
                amount_debited=float(payment.get("efectivo")[0]),
                amount_refunded=float(payment.get("efectivo")[0]) - float(total.incl_tax),
                reference=reference)
            self.add_payment_source(source)

            # Record payment event
            self.add_payment_event('auth', total.incl_tax)
        else:
            reference="pagoTarjetaOffline"
            source_type, __ = models.SourceType.objects.get_or_create(
                name="PagoTarjeta")
            source = models.Source(
                source_type=source_type,
                amount_allocated=total.incl_tax,
                reference=reference)
            self.add_payment_source(source)

            # Record payment event
            self.add_payment_event('auth', total.incl_tax)
            #raise RedirectRequired(facade.BillingFacade().get_redirect_url(order_number, total.incl_tax,"123123","123"))
    # Payment successful! Record payment source
