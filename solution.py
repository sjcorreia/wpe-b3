#!/usr/bin/env python
from collections import Counter
from typing import List, Dict, Any


class Serializable(object):
    pass


class JSONMixin(Serializable):
    pass


class XMLMixin(Serializable):
    pass


class CSVMixin(Serializable):
    pass
