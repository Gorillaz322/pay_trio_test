from flask import jsonify
from flask_views.edit import FormView

from app import app
from .forms import InvoiceForm


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
            return self.redirect_to_payment_page()
        else:
            return self.request_invoice()

    def redirect_to_payment_page(self):
        pass

    def request_invoice(self):
        pass


app.add_url_rule(
    '/',
    view_func=InvoiceView.as_view('invoice_view')
)