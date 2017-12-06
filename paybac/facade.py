from django.core.urlresolvers import reverse
from oscar.apps.payment.exceptions import PaymentError
import hashlib
import datetime

class BillingFacade(object):

    def get_redirect_url(self, order_number, total_incl_tax,ccnumber,ccexp):
        url = "https://credomatic.compassmerchantsolutions.com/api/transact.php?hash={0}&time={1}&ccnumber={2}&ccexp={3}&amount={4}&type={5}&orderid={6}&key_id={7}&cvv={8}&redirect={9}".encode("utf")
        return url.format(hashlib.md5("123123").hexdigest(),datetime.datetime.now(),"123123123","123",str(total_incl_tax),"SALE",order_number,"ASD12312","123","http://localhost:8000/confirm/")


def confirm(request):

    params = {
            'response': request.GET.get('response',None),
            'responsetext': request.GET.get('responsetext',None),
            'authcode': request.GET.get('authcode',None),
            'transactionid': request.GET.get('transactionid',None),
            'avsresponse': request.GET.get('avsresponse',None),
            'cvvresponse': request.GET.get('cvvresponse',None),
            'orderid': request.GET.get('orderid',None),
            'type': request.GET.get('type',None),
            'response_code': request.GET.get('response_code',None),
            'amount': request.GET.get('amount',None),
            'hash': request.GET.get('hash',None),
            'time': request.GET.get('time',None),
    }

    if(params["response"] != "1" and params["response_code"] != "100"):
        raise PaymentError(params["responsetext"])
