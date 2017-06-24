#!/usr/bin/env python
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4
# Please do not change the two lines above. See PEP 8, PEP 263.
'''Delete an object of type: saved_question'''
__author__ = 'Jim Olsen <jim.olsen@tanium.com>'
__version__ = '2.1.5'

import pytan.lib.pytan.binsupport as binsupport

def main():
    binsupport.version_check(reqver=__version__)

    parser = binsupport.setup_delete_object_argparser(obj='saved_question', doc=__doc__)
    args = parser.parse_args()

    handler = binsupport.process_handler_args(parser=parser, args=args)
    response = binsupport.process_delete_object_args(
        parser=parser, handler=handler, obj='saved_question', args=args,
    )

if __name__ == "__main__":
    main()
