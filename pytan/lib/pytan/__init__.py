# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4
# Please do not change the two lines above. See PEP 8, PEP 263.
'''A python package that makes using the Tanium Server SOAP API easy.'''

__title__ = 'PyTan'
__version__ = '2.1.8'
"""
Version of PyTan
"""

__author__ = 'Jim Olsen <jim.olsen@tanium.com>'
"""
Author of Pytan
"""

__license__ = 'MIT'
"""
License for PyTan
"""

__copyright__ = 'Copyright 2015 Tanium'
"""
Copyright for PyTan
"""

import sys
import os

import pytan  # noqa
from pytan.lib import taniumpy # noqa
from pytan.lib.pytan import xml_clean # noqa
from pytan.lib.pytan import exceptions  # noqa
from pytan.lib.pytan import utils  # noqa
from pytan.lib.pytan import constants  # noqa
from pytan.lib.pytan import pollers  # noqa
from pytan.lib.pytan import sessions  # noqa
from pytan.lib.pytan import help  # noqa
from pytan.lib.pytan.handler import Handler  # noqa


# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
