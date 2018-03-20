import uuid

from flask import render_template, redirect
from flask_views.edit import FormView
import requests

from app import app
from .forms import InvoiceForm
from .utils import get_hash, CURRENCY_CODES
import settings


class InvoiceView(FormView):
    form_class = InvoiceForm
    template_name = 'InvoiceView.html'

    def return_error(self, errors):
        return render_template('InvoiceView.html', form=self.form_class(), errors=errors)

    def form_invalid(self, form):
        return self.return_error({key: value[0] for key, value in form.errors.items()})

    def form_valid(self, form):
        if form.currency.data == "usd":
            return self.create_invoice_via_tip(form)
        else:
            return self.create_invoice_via_api(form)

    def create_invoice_via_tip(self, form):
        data = dict(
            amount=form.amount.data,
            currency=CURRENCY_CODES[form.currency.data],
            shop_id=settings.SHOP_ID,
            shop_invoice_id=uuid.uuid4()
        )

        data.update(dict(
            sign=get_hash(**data),
            description=form.description.data))

        return render_template('InvoiceConfirmationView.html', **data, currency_text=form.currency.data)

    def create_invoice_via_api(self, form):
        data = dict(
            amount=form.amount.data,
            currency=CURRENCY_CODES[form.currency.data],
            shop_id=settings.SHOP_ID,
            shop_invoice_id=uuid.uuid4(),
            payway='payeer_eur'
        )

        data.update(dict(sign=get_hash(**data)))

        response = requests.post('https://central.pay-trio.com/invoice',
                                 headers={"Content-Type": "application/json"},
                                 json=data)

        if response.status_code == 200:
            return redirect(response.json()['data']['data']['referer'])
        else:
            return self.return_error({"Response": response.json()['data']['message']})

app.add_url_rule(
    '/',
    view_func=InvoiceView.as_view('invoice_view')
)