from flask import jsonify, render_template
from flask_views.edit import FormView

from app import app
from .forms import InvoiceForm
from .utils import get_hash, CURRENCY_CODES
import settings


class InvoiceView(FormView):
    form_class = InvoiceForm
    template_name = 'InvoiceView.html'

    def form_invalid(self, form):
        return jsonify({
            'status': 'error',
            'errors': form.errors
        })

    def form_valid(self, form):
        if form.currency.data == "usd":
            return self.confirm_invoice_request(form)
        else:
            return self.request_invoice()

    def confirm_invoice_request(self, form):
        data = dict(
            amount=form.amount.data,
            currency=CURRENCY_CODES[form.currency.data],
            shop_id=settings.SHOP_ID,
            shop_invoice_id=1
        )

        data.update(dict(
            sign=get_hash(**data),
            description=form.description.data))

        return render_template('InvoiceConfirmationView.html', **data)

    def request_invoice(self):
        pass


app.add_url_rule(
    '/',
    view_func=InvoiceView.as_view('invoice_view')
)