#!/usr/bin/env python -i
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4
# Please do not change the two lines above. See PEP 8, PEP 263.
import os
import sys
import logging
sys.dont_write_bytecode = True
my_file = os.path.abspath(__file__)
my_dir = os.path.dirname(my_file)
parent_dir = os.path.dirname(my_dir)
path_adds = [parent_dir]

for aa in path_adds:
    if aa not in sys.path:
        sys.path.append(aa)


# adds readline, autocomplete, history to python interactive console
import atexit
import os
import sys
import pprint
import code

try:
    import readline
    import rlcompleter
except:
    pass

sys.dont_write_bytecode = True


def debug_list(debuglist):
    for x in debuglist:
        debug_obj(x)


def debug_obj(debugobj):
    pprint.pprint(vars(debugobj))


# Utility function to dump all info about an object
def introspect(obj, depth=0):
    import types
    print "%s%s: %s\n" % (depth * "\t", obj, [
        x for x in dir(obj) if x[:2] != "__"])
    depth += 1
    for x in dir(obj):
        if x[:2] == "__":
            continue
        subobj = getattr(obj, x)
        print "%s%s: %s" % (depth * "\t", x, subobj)
        if isinstance(subobj, types.InstanceType) and dir(subobj) != []:
            introspect(subobj, depth=depth + 1)
            print


class HistoryConsole(code.InteractiveConsole):
    def __init__(self, locals=None, filename="<console>",
                 histfile=os.path.expanduser("~/.console-history")):
        code.InteractiveConsole.__init__(self, locals, filename)
        try:
            self.init_history(histfile)
        except:
            pass

    def init_history(self, histfile):
        if 'libedit' in readline.__doc__:
            # osx style readline
            readline.parse_and_bind("bind ^I rl_complete")
            readline.parse_and_bind("bind ^R em-inc-search-prev")
        else:
            # unix style readline
            readline.parse_and_bind("tab: complete")
        if hasattr(readline, "read_history_file"):
            try:
                readline.read_history_file(histfile)
            except IOError:
                pass
            atexit.register(self.save_history, histfile)

    @staticmethod
    def save_history(histfile):
        readline.write_history_file(histfile)


console = HistoryConsole()

logging.basicConfig(level=logging.DEBUG)

# hide auth messages that are below warn (change to DEBUG to see them)
logging.getLogger('api.session.auth').setLevel(logging.WARN)

# show http debug messages
logging.getLogger('api.session.http').setLevel(logging.WARN)

# hide http.body messages that are below warn (change to DEBUG to see them)
logging.getLogger('api.session.http.body').setLevel(logging.WARN)


import api

host = '172.16.31.128'
username = 'Tanium User'
password = 'T@n!um'

session = api.Session(host)
print session
session.authenticate(username, password)
print session