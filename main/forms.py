from flask_wtf import Form
from wtforms import FloatField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class InvoiceForm(Form):
    CURRENCY_TYPES = (
        ('usd', 'USD'),
        ('eur', 'Euro')
    )

    amount = FloatField('Amount',
                        validators=[DataRequired(),
                                    NumberRange(min=0, max=15000)])

    currency = RadioField('Currency',
                          choices=[*CURRENCY_TYPES],
                          validators=[DataRequired()])

    description = TextAreaField('Description',
                                validators=[Length(max=5000)])