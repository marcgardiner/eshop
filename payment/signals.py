from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from io import BytesIO

from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
import weasyprint

from orders.models import Order

def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        order = get_object_or_404(Order, id=ipn_obj.invoic)
        order.paid = True
        order.save()
        subject = 'e - shop - Invoic no. {}'.format(order.id)
        message = 'Please, find attached the invoice for your recent purchase.'
        email = EmailMessage(subject, message, 'admin@eshop.com', [order.email])
        html = render_to_string('orders/order/pdf.html', {'order': order})
        out = BytesIO()
        stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
        weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
        email.attach('order_{}.pdf'.format(order.id), out.getvalue(), 'application/pdf')
        email.send()
valid_ipn_received.connect(payment_notification )