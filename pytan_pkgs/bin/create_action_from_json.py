#!/usr/bin/env python
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4
# Please do not change the two lines above. See PEP 8, PEP 263.
'''Create an object of type: action from a JSON file'''
__author__ = 'Jim Olsen <jim.olsen@tanium.com>'
__version__ = '2.1.5'

import os
import sys
from pytan_pkgs.lib.pytan import binsupport

def main():
    my_name = os.path.splitext(os.path.basename(__file__))
    binsupport.version_check(reqver=__version__)

    parser = binsupport.setup_create_json_object_argparser(obj='action', doc=__doc__)
    args = parser.parse_args()

    handler = binsupport.process_handler_args(parser=parser, args=args)
    response = binsupport.process_create_json_object_args(
        parser=parser, handler=handler, obj='action', args=args,
    )

if __name__ == "__main__":
    main()
