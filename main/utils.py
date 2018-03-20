from collections import OrderedDict
import hashlib

import settings

CURRENCY_CODES = {
    'usd': 840,
    'eur': 978
}


def get_hash(**kwargs):
    sorted_kwargs = OrderedDict(sorted(kwargs.items()))

    h = ':'.join([str(v) for k, v in sorted_kwargs.items()])
    h += settings.PAY_TRIO_SECRET_KEY

    md5 = hashlib.md5()
    md5.update(h.encode('utf-8'))

    return md5.hexdigest()
