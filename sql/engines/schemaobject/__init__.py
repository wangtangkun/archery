#!/usr/bin/python
# coding:utf-8
__author__ = 'Mitch Matuson, Mustafa Ozgur'
__copyright__ = """
Copyright 2009-2016 Mitch Matuson
Copyright 2016 Mustafa Ozgur
"""
__version__ = "0.5.10"
__license__ = "Apache 2.0"

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# shortcut to SchemaObject()
from schemaobject.schema import SchemaObject
