from oscar.apps.checkout.forms import ShippingAddressForm,GatewayForm
from django import forms

class GatewayForm(GatewayForm):
    username = forms.EmailField(label=("Mi correo es:"))
    GUEST, NEW, EXISTING = 'anonymous', 'new', 'existing'
    CHOICES = (
        (GUEST, ('Comprar sin registrarme')),)
    options = forms.ChoiceField(widget=forms.widgets.RadioSelect,
                                choices=CHOICES, initial=GUEST)


class ShippingAddressForm(ShippingAddressForm):

    class Meta(ShippingAddressForm.Meta):
        fields = [
            'first_name','line1', 'line2', 'line4',
            'state','country',
            'phone_number', 'notes',
        ]
