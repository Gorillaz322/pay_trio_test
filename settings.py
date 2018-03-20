import os

SECRET_KEY = os.environ.get('SECRET_KEY')

PAY_TRIO_SECRET_KEY = os.environ.get('PAY_TRIO_SECRET_KEY')

SHOP_ID = int(os.environ.get('SHOP_ID'))