#!/usr/bin/env python
import csv
import json
import pickle
import xml.etree.ElementTree as ET
from collections import Counter
from typing import List, Dict, Any


class Serializable():
    """docstring """
    def dump(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.__dict__, file, pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        return self.__dict__.update(pickle.load(open(filename, 'rb')))


class JSONMixin(Serializable):
    """docstring"""
    def dump(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file, sort_keys=True)

    def load(self, filename):
        with open(filename, 'rb') as file:
            return self.__dict__.update(json.load(file))


class XMLMixin(Serializable):
    pass


class CSVMixin(Serializable):
    """docstring"""
    def load(self, filename):
        with open(filename, newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                self.__dict__.update(row)

    def dump(self, filename):
        with open(filename, 'w', newline='') as csvFile:
            field_names = self.__dict__.keys()
            writer = csv.DictWriter(csvFile, field_names)
            writer.writerow(self.__dict__)
