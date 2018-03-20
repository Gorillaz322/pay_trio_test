import logging

from flask import Flask

app = Flask(__name__, static_url_path='/static')

app.debug = True
app.config.from_object('settings')

logger = logging.getLogger('pay_trio_test')
console_logging = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
console_logging.setFormatter(formatter)
logger.addHandler(console_logging)
logger.setLevel(logging.INFO)

import main.views
