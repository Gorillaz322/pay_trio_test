from collections import OrderedDict
import hashlib

import settings


def get_hash(**kwargs):
    sorted_kwargs = OrderedDict(sorted(kwargs.items()))

    h = ':'.join(sorted_kwargs.keys())
    h += settings.PAY_TRIO_SECRET_KEY

    md5 = hashlib.md5()
    md5.update(h.encode('utf-8'))

    return md5.hexdigest()
