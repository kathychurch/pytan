#!/usr/bin/env python
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4
# Please do not change the two lines above. See PEP 8, PEP 263.
'''Ask a saved question and save the results as a report format'''
__author__ = 'Jim Olsen <jim.olsen@tanium.com>'
__version__ = '2.1.5'

import os
import sys
import pytan.lib.pytan.binsupport as binsupport

def main():
    my_name = os.path.splitext(os.path.basename(__file__))

    binsupport.version_check(reqver=__version__)

    setupmethod = getattr(binsupport, 'setup_{}_argparser'.format(my_name))
    responsemethod = getattr(binsupport, 'process_{}_args'.format(my_name))

    parser = setupmethod(doc=__doc__)
    args = parser.parse_args()

    handler = binsupport.process_handler_args(parser=parser, args=args)
    response = responsemethod(parser=parser, handler=handler, args=args)

if __name__ == "__main__":
    main()
