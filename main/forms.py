from flask_wtf import Form
from wtforms import FloatField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length


class InvoiceForm(Form):
    CURRENCY_TYPES = (
        ('usd', 'USD'),
        ('eur', 'Euro')
    )

    amount = FloatField('Amount',
                        validators=[DataRequired()])

    currency = RadioField('Currency',
                          choices=[*CURRENCY_TYPES],
                          validators=[DataRequired()])

    description = TextAreaField('Description',
                                validators=[Length(max=5000)])