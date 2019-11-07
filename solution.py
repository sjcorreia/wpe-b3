#!/usr/bin/env python
import json
import pickle
from collections import Counter
from typing import List, Dict, Any


class Serializable(object):
    def dump():
        pass

    def load():
        pass


class JSONMixin(Serializable):
    pass


class XMLMixin(Serializable):
    pass


class CSVMixin(Serializable):
    pass
